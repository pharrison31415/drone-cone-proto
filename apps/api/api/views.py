from functools import partial
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from .views_utils import JsonResponse, safe_querey, verify_token, CUSTOMER_USER, MANAGER_USER, OWNER_USER, verify_customer_token, verify_manager_token, verify_owner_token, optional_customer_token, verify_order_token, user_login, new_user
from datetime import datetime, timezone
import json

from api.models import DroneStatus, Drone, DroneType, Customer, Manager, Owner, OrderStatus, CustomerToken, ManagerToken, OwnerToken, Address, Cone, ConeType, IceCreamType, ToppingType, Order, Delivery, Message, ManagerRevenue, ManagerCost, OrderToken


def hello_world(request):
    return JsonResponse({"helloWorld": False})


def get_delivery_count(request):
    delivery_count = len(Delivery.objects.all())
    return JsonResponse({"deliveryCount": delivery_count})


def get_drone_statuses(request):
    statuses = DroneStatus.objects.all()
    return JsonResponse({"success": True,
                        "droneStatuses": [status.toJSON() for status in statuses]})


def get_drone_types(request):
    drone_types = DroneType.objects.all()
    return JsonResponse({"success": True,
                        "droneTypes": [drone_type.toJSON() for drone_type in drone_types]})

@verify_manager_token
def get_messages(request):
    messages = Message.objects.all()
    return JsonResponse({"success": True,
                         "messages": [messages.toJSON() for message in messages]})

@csrf_exempt
def new_customer(request):
    return partial(new_user, user_type=CUSTOMER_USER)(request)


@csrf_exempt
def new_manager(request):
    return partial(new_user, user_type=MANAGER_USER)(request)


@csrf_exempt
def new_owner(request):
    return partial(new_user, user_type=OWNER_USER)(request)


@csrf_exempt
def customer_login(request):
    return partial(user_login, user_type=CUSTOMER_USER)(request)


@csrf_exempt
def manager_login(request):
    return partial(user_login, user_type=MANAGER_USER)(request)


@csrf_exempt
def owner_login(request):
    return partial(user_login, user_type=OWNER_USER)(request)


@verify_customer_token
def get_my_addresses(request, user):
    addresses = Address.objects.filter(customer=user, deleted=False)
    return JsonResponse({
        "success": True,
        "addresses": [
            a.toJSON() for a in addresses
        ]
    })


@csrf_exempt
@verify_customer_token
def post_address(request, user):
    body = json.loads(request.body)
    new_addr = Address(
        line_one=body['lineOne'],
        line_two=body['lineTwo'],
        city=body['city'],
        state=body['state'],
        zip_code=body['zipCode'],
        customer=user
    )
    new_addr.save()
    return JsonResponse({'success': True, 'id': new_addr.id})


@csrf_exempt
@verify_customer_token
def delete_address(request, user):
    body = json.loads(request.body)

    address, address_found = safe_querey(
        Address, id=body["addressId"], customer=user, deleted=False)
    if not address_found:
        return JsonResponse({
            'success': False,
            'message': 'no address found'
        })

    address.deleted = True
    address.save()

    return JsonResponse({'success': True})


def get_cone_types(request):
    return JsonResponse({'success': True, 'coneTypes': [
        i.toJSON_customer() for i in ConeType.objects.all()
    ]})


def get_ice_cream_types(request):
    return JsonResponse({'success': True, 'iceCreamTypes': [
        i.toJSON_customer() for i in IceCreamType.objects.all()
    ]})


def get_topping_types(request):
    return JsonResponse({'success': True, 'toppingTypes': [
        i.toJSON_customer() for i in ToppingType.objects.all()
    ]})


@verify_manager_token
def get_inventory(request, user):
    """
        how much of each type of ice cream is left
        how much of each type of cone is left
        how much of each type of topping is left
        what the unit price of each item is
    """
    models = [ConeType, IceCreamType, ToppingType]
    keys = ["coneTypes", "iceCreamTypes", "toppingTypes"]
    inventory = {}
    for model, key in zip(models, keys):
        inventory[key] = [i.toJSON_manager() for i in model.objects.all()]

    return JsonResponse({"success": True, "inventory": inventory})


def finances(request):
    response = JsonResponse({'status': 'unable to access database'})
    # TODO get request for the money spent and made - does revenue have it's own model or is it with inventory?
    return response


@csrf_exempt
@verify_manager_token
def purchase_inventory(request, user):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })

    body = json.loads(request.body)
    item_type = ""
    types = {"coneType": ConeType, "iceCreamType": IceCreamType,
             "toppingType": ToppingType}
    if "itemType" in body:
        item_type = body["itemType"]
        if item_type not in types:
            return JsonResponse({"success": False, "message": "itemType not found"})
    else:
        return JsonResponse({"success": False, "message": "itemType not found"})
    item, item_found = safe_querey(types[item_type], name=body["name"])
    if not item_found:
        return JsonResponse({"success": False, "message": "item not found"})

    if "additionalUnits" in body:
        item.quantity += body["additionalUnits"]
        ManagerCost(
            amount=int(body["additionalUnits"] * item.unit_cost),
            message=f"{body['additionalUnits']} units of {item.name}"
        ).save()
    else:
        return JsonResponse({"success": False, "message": "additionalUnits not found"})
    item.save()
    return JsonResponse({'success': True})


@csrf_exempt
@verify_manager_token
def update_inventory(request, user):
    if request.method != "PATCH":
        return JsonResponse({
            'success': False,
            'message': 'PATCH method required'
        })

    body = json.loads(request.body)
    # item = ConeType.objects.filter(id=body['id'])
    if "itemType" in body:
        itemType = body["itemType"]
        types = ["coneType", "iceCreamType", "toppingType"]
        if itemType not in types:
            return JsonResponse({"success": False, "message": "item type not found"})
    else:
        return JsonResponse({"success": False, "message": "item type not found"})
    item, item_found = safe_querey(itemType, name=body["name"])
    if not item_found:
        return JsonResponse({"success": False, "message": "item not found"})

    if "unitCost" in body:
        item.unit_cost = body["unitCost"]
    item.save()
    return JsonResponse({'success': True})


@csrf_exempt
@verify_owner_token
def add_drone(request, user):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })

    body = json.loads(request.body)
    status = get_object_or_404(DroneStatus, text=body['status'])
    drone_type = get_object_or_404(DroneType, text=body['droneType'])

    new_drone = Drone(
        name=body['name'],
        status=status,
        drone_type=drone_type,
        owner=user
    )
    new_drone.save()

    return JsonResponse({'success': True, 'id': new_drone.id})


@verify_owner_token
def get_my_drones(request, user):
    drones = Drone.objects.filter(owner=user)
    return JsonResponse({
        "success": True,
        "drones": [
            d.toJSON() for d in drones
        ]
    })


@csrf_exempt
@verify_owner_token
def update_drone(request, user):
    if request.method != "PATCH":
        return JsonResponse({
            'success': False,
            'message': 'PATCH method required'
        })

    body = json.loads(request.body)
    drone, drone_found = safe_querey(Drone, id=body["id"])
    if not drone_found or drone.owner != user:
        return JsonResponse({"success": False, "message": "drone does not exist"})

    if "name" in body:
        drone.name = body["name"]
    if "status" in body:
        if drone.status.text == "delivering":
            return JsonResponse({"success": False, "message": "Drone is delivering. Status cannot be updated."})
        drone.status = get_object_or_404(DroneStatus, text=body["status"])
    if "droneType" in body:
        drone.drone_type = get_object_or_404(DroneType, text=body["droneType"])

    drone.save()
    return JsonResponse({"success": True, "id": drone.id})


@verify_customer_token
def get_past_orders(request, user):
    # return the users past orders
    orders = Order.objects.filter(customer=user)
    orders_json_list = []
    for order in orders:
        deliveries = Delivery.objects.filter(order=order)
        cones = []
        for delivery in deliveries:
            cone_query_set = Cone.objects.filter(delivery=delivery)
            cones += [cone.toJSON() for cone in cone_query_set]

        order_json = order.toJSON()
        order_json["cones"] = cones

        orders_json_list.append(order_json)
    from pprint import pprint
    pprint(orders_json_list)

    return JsonResponse({
        "success": True,
        "orders": orders_json_list,
    })


@csrf_exempt
@optional_customer_token
def new_order(request, user_found, user):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })

    body = json.loads(request.body)

    # Get the drones to use, throw error if not enough
    idle_status = DroneStatus.objects.get(text="idle")
    drones_available = list(Drone.objects.order_by(
        "last_use").filter(status=idle_status))
    drones_using = []
    cones_remaining = len(body["cones"])
    if cones_remaining < 1:
        return JsonResponse({
            "success": False,
            "message": "order at least one cone"
        })

    while cones_remaining > 0:
        if not drones_available:
            return JsonResponse({
                "success": False,
                "message": "not enough available drones"
            })
        next_drone = drones_available.pop(0)
        drones_using.append(next_drone)
        cones_remaining -= next_drone.drone_type.capacity

    # handle addressing: customer user or guest
    address = None
    if user_found:
        address, address_found = safe_querey(
            Address, id=body["addressId"], customer=user, deleted=False)
        if not address_found:
            return JsonResponse({
                'success': False,
                'message': 'no address found'
            })
    else:
        address = Address(
            line_one=body["guestAddress"]["lineOne"],
            line_two=body["guestAddress"]["lineTwo"],
            city=body["guestAddress"]["city"],
            state=body["guestAddress"]["state"],
            zip_code=body["guestAddress"]["zipCode"],
            customer=None
        )
        address.save()

    # check that we have stock
    for cone in body["cones"]:
        if get_object_or_404(ConeType, name=cone["coneType"]).quantity <= 0 or \
                get_object_or_404(IceCreamType, name=cone["iceCreamType"]).quantity <= 0 or \
                get_object_or_404(ToppingType, name=cone["toppingType"]).quantity <= 0:
            return JsonResponse({"success": False, "message": "not enough stock to make order"})

    # find price
    PRICE_PER_CONE = 250
    price = len(body["cones"]) * PRICE_PER_CONE

    # find cost
    cost = 0
    for cone in body["cones"]:
        cost += sum([
            get_object_or_404(ConeType, name=cone["coneType"]).unit_cost,
            get_object_or_404(
                IceCreamType, name=cone["iceCreamType"]).unit_cost,
            get_object_or_404(ToppingType, name=cone["toppingType"]).unit_cost,
        ])

    new_order = Order(
        customer=(user if user_found else None),
        address=address,
        price=price,
        cost=cost,
        status=OrderStatus.objects.get(text="delivering")
    )
    new_order.save()

    # handle manager revenue
    MANAGER_DRONE_REVENUE_SPLIT = 0.5
    revenue_remaining = price - cost

    # create droneorders, cones
    cone_index = 0
    delivering_status = DroneStatus.objects.get(text="delivering")
    for drone in drones_using:
        drone.status = delivering_status
        drone.last_use = datetime.now(timezone.utc)
        new_delivery = Delivery(
            drone=drone,
            order=new_order,
        )
        new_delivery.save()
        for i in range(cone_index, cone_index + drone.drone_type.capacity):
            if i >= len(body["cones"]):
                break
            cone_type = get_object_or_404(
                ConeType, name=body["cones"][i]["coneType"])
            ice_cream_type = get_object_or_404(
                IceCreamType, name=body["cones"][i]["iceCreamType"])
            topping_type = get_object_or_404(
                ToppingType, name=body["cones"][i]["toppingType"])
            Cone(
                delivery=new_delivery,
                cone_type=cone_type,
                ice_cream_type=ice_cream_type,
                topping_type=topping_type,
            ).save()

            cone_type.quantity -= 1
            cone_type.save()
            ice_cream_type.quantity -= 1
            ice_cream_type.save()
            topping_type.quantity -= 0 if topping_type.name == "No topping" else 1
            topping_type.save()

            cone_revenue = int(
                PRICE_PER_CONE * (1-MANAGER_DRONE_REVENUE_SPLIT))
            revenue_remaining -= cone_revenue
            drone.revenue += cone_revenue

        drone.save()
        cone_index += drone.drone_type.capacity

    ManagerRevenue(
        amount=revenue_remaining,
        message=f"order id: {new_order.id}"
    ).save()

    response = JsonResponse({
        "success": True,
        "orderId": new_order.id,
        "created": new_order.created
    })
    token = get_random_string(length=128)
    OrderToken(
        token=token,
        order=new_order
    ).save()
    response.headers["Set-Cookie"] = f"order-token={token}; Path=/"

    return response


@csrf_exempt
@verify_order_token
def order_delivered(request, order):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })

    deliveries = Delivery.objects.filter(order=order)
    idle_status = DroneStatus.objects.get(text="idle")
    delivered_status = OrderStatus.objects.get(text="delivered")
    for delivery in deliveries:
        delivery.drone.status = idle_status
        delivery.drone.save()

        delivery.order.status = delivered_status
        delivery.order.delivered_at = datetime.now(timezone.utc)
        delivery.order.save()

    return JsonResponse({"success": True})


@verify_customer_token
def private_customer_data(request, user):
    return JsonResponse({
        "success": True,
        "user": user.toJSON()
    })


@verify_manager_token
def private_manager_data(request, user):
    return JsonResponse({
        "success": True,
        "user": user.toJSON(),
    })


@verify_owner_token
def private_owner_data(request, user):
    return JsonResponse({
        "success": True,
        "user": user.toJSON()
    })


@verify_manager_token
def get_manager_revenues(request, user):
    revenues = ManagerRevenue.objects.all()
    return JsonResponse({
        "success": True,
        "revenues": [r.toJSON() for r in revenues]
    })


@verify_manager_token
def get_manager_costs(request, user):
    costs = ManagerCost.objects.all()
    return JsonResponse({
        "success": True,
        "costs": [c.toJSON() for c in costs]
    })


@csrf_exempt
def new_message(request):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })

    body = json.loads(request.body)

    Message(
        content=body["content"],
        email=body["email"]
    ).save()

    return JsonResponse({"success": True})

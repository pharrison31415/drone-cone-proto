from functools import partial
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .views_utils import JsonResponse, safe_querey, verify_token, CUSTOMER_USER, MANAGER_USER, OWNER_USER, verify_customer_token, verify_manager_token, verify_owner_token, optional_customer_token, verify_order_token, user_login, new_user
from datetime import datetime
import json

from api.models import DroneStatus, Drone, DroneType, Customer, Manager, Owner, OrderStatus, CustomerToken, ManagerToken, OwnerToken, Address, Cone, ConeType, IceCreamType, ToppingType, Order, DroneOrder, Message


def hello_world(request):
    return JsonResponse({"helloWorld": False})


def get_drone_statuses(request):
    statuses = DroneStatus.objects.all()
    return JsonResponse({"droneStatuses": [status.toJSON() for status in statuses]})


def get_drone_types(request):
    drone_types = DroneType.objects.all()
    return JsonResponse({"droneTypes": [drone_type.toJSON() for drone_type in drone_types]})

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
    addresses = Address.objects.filter(customer=user)
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


def get_cone_types(request):
    return JsonResponse({'success': True, 'coneTypes': [
        i.toJSON() for i in ConeType.objects.all()
    ]})

def get_ice_cream_types(request):
    return JsonResponse({'success': True, 'iceCreamTypes': [
        i.toJSON() for i in IceCreamType.objects.all()
    ]})

def get_topping_types(request):
    return JsonResponse({'success': True, 'toppingTypes': [
        i.toJSON() for i in ToppingType.objects.all()
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
        inventory[key] = [ i.toJSON_manager() for i in model.objects.all() ]

    return JsonResponse({"success": True, "inventory": inventory})


def finances(request):
    response = JsonResponse({'status': 'unable to access database'})
    #TODO get request for the money spent and made - does revenue have it's own model or is it with inventory?
    return response

@csrf_exempt
@verify_manager_token
def update_inventory(request):
    if request.method != "PATCH":
        return JsonResponse({
            'success': False,
            'message': 'PATCH method required'
        })
    body = json.loads(request.body)
    item = ConeType.objects.filter(id=body['id'])
    if "amountChange" in body:
        item.quantity += body["amountChange"]  
    if "price" in body:
        item.unit_cost = body["price"]
    if "name" in body:
        item.name = body["name"]
    item.save()
    response = JsonResponse({'success': True})
    return response
"""
    price per unit
    added inventory
    changed types of cones
    changed types of ice cream
    changed types of toppings
"""

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
    drone = Drone.objects.filter(id=body["id"])

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

#TODO add all the information a customer will see **
"""
    first and last name
    username
    past orders
    password?
"""

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
    drones_available = list(Drone.objects.order_by("last_use").filter(status=idle_status))
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
        address, address_found = safe_querey(Address, id=body["addressId"], customer=user)
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

    # find cost
    cost = 0
    for cone in body["cones"]:
        cost += sum([
            get_object_or_404(ConeType, name=cone["coneType"]).unit_cost,
            get_object_or_404(IceCreamType, name=cone["iceCreamType"]).unit_cost,
            get_object_or_404(ToppingType, name=cone["toppingType"]).unit_cost,
        ])

    # markup cost for price
    price = int(cost * 1.10)

    new_order = Order(
        customer=(user if user_found else None),
        address=address,
        price=price,
        cost=cost,
        status=OrderStatus.objects.get(text="delivering")
    )
    new_order.save()
    

    # create droneorders, cones
    cone_index = 0
    delivering_status = DroneStatus.objects.get(text="delivering")
    for drone in drones_using:
        drone.status = delivering_status
        drone.last_use = datetime.now()
        drone.save()
        new_drone_order = DroneOrder(
            drone=drone,
            order=new_order,
        )
        new_drone_order.save()
        for i in range(cone_index, cone_index + drone.drone_type.capacity):
            if i >= len(body["cones"]):
                break
            Cone(
                drone_order=new_drone_order,
                cone_type=get_object_or_404(ConeType, name=body["cones"][i]["coneType"]),
                ice_cream_type=get_object_or_404(IceCreamType, name=body["cones"][i]["iceCreamType"]),
                topping_type=get_object_or_404(ToppingType, name=body["cones"][i]["toppingType"]),
            ).save()
        cone_index += drone.drone_type.capacity

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
    response.headers["Set-Cookie"] = f"order-token={token}" 

    return response

@csrf_exempt
@verify_order_token
def order_delivered(request, order):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })

    drone_orders = DroneOrder.objects.filter(order=order)
    idle_status = DroneStatus.objects.get(text="idle")
    delivered_status = OrderStatus.objects.get(text="delivered")
    for drone_order in drone_orders:
        drone_order.drone.status = idle_status
        drone_order.drone.save()

        drone_order.order.status = delivered_status
        drone_order.order.save()

    return JsonResponse({ "success": True })


@verify_customer_token
def private_customer_data(request, user):
    response = user.toJSON()
    data = response.content
    addresses = []
    for address in Address:
        if address.customer == user.pk:
            address_data = address.toJSON.content
            addresses.append(address_data)
    data.update({"addresses" : addresses})
    response.content = data
    return response

@verify_manager_token
def private_manager_data(request, user):
    return user.toJSON()

@verify_owner_token
def private_owner_data(request, user):
    return user.toJSON()


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
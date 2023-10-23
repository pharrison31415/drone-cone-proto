from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string

from api.models import DroneStatus, DroneType, Customer, CustomerToken


def safe_querey(table, **kwargs):
    querey_set = table.objects.filter(**kwargs)
    if not querey_set:
        return None, False

    return querey_set[0], True


def verify_customer_token(view):
    def wrapper_verify(*args, **kwargs):
        customer_token = args[0].COOKIES.get("customer-token", False)
        retrieved_token, found = safe_querey(
            CustomerToken, token=customer_token)
        if not found:
            return JsonResponse({'success': False, 'message': 'bad customer token'})

        return view(*args, customer=retrieved_token.customer, **kwargs)

    return wrapper_verify


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
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required. Do not use these credentials.'
        })

    _, username_taken = safe_querey(Customer, pk=request.POST['username'])
    if username_taken:
        return JsonResponse({
            'success': False,
            'message': 'username taken'
        })

    Customer(
        username=request.POST['username'],
        password_hash=make_password(request.POST['password']),
        first_name=request.POST['firstName'],
        last_name=request.POST['lastName'],
    ).save()

    return JsonResponse({'success': True})


@csrf_exempt
def customer_login(request):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required.',
        })

    customer, customer_found = safe_querey(
        Customer, pk=request.POST['username'])
    # susceptible to timing attack
    if not customer_found or not check_password(request.POST['password'], customer.password_hash):
        return JsonResponse({
            'success': False,
            'message': 'bad login',
        })

    response = JsonResponse({'success': True})
    token = get_random_string(length=128)
    CustomerToken(
        token=token,
        customer=customer
    ).save()
    response.headers["Set-Cookie"] = f"customer-token={token}"

    return response



@csrf_exempt
def manager_login(request):
	if request.method != "POST":
		return JsonResponse({
			'success': False,
			'message': 'POST method required.',
		})
	#import the manager database to complete
	return



#TODO post request for a new order, update inventory - from customer
#TODO get request for things available to order (including prices) - for customer
#TODO get request for what's in the inventory (including prices) - for manager
"""
    how much of each type of ice cream is left
    how much of each type of cone is left
    how much of each type of topping is left
    what the unit price of each item is

TODO get request for the money spent and made - does revenue have it's own model or is it with inventory?

"""
#TODO post request for update inventory - from manager
"""
    price per unit
    added inventory
    changed types of cones
    changed types of ice cream
    changed types of toppings
"""
#TODO post request for new drone (with what's available) **

#TODO add all the information a customer will see **
"""
    first and last name
    username
    past orders
    password?
"""
@verify_customer_token
def private_customer_data(request, customer):
    return JsonResponse({"firstName": customer.first_name})


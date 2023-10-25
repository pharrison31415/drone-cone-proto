from functools import partial
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from .views_utils import safe_querey, verify_token, CUSTOMER_USER, MANAGER_USER, OWNER_USER, verify_customer_token, verify_manager_token, verify_owner_token, user_login

from api.models import DroneStatus, DroneType, Customer, Manager, Owner, CustomerToken, ManagerToken, OwnerToken


def hello_world(request):
    return JsonResponse({"helloWorld": False})


def get_drone_statuses(request):
    statuses = DroneStatus.objects.all()
    return JsonResponse({"droneStatuses": [status.toJSON() for status in statuses]})


def get_drone_types(request):
    drone_types = DroneType.objects.all()
    return JsonResponse({"droneTypes": [drone_type.toJSON() for drone_type in drone_types]})


def new_user(request, user_type):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required. Do not use these credentials.'
        })

    _, username_taken = safe_querey(user_type["user_model"], pk=request.POST['username'])
    if username_taken:
        return JsonResponse({
            'success': False,
            'message': 'username taken'
        })
    
    user_type["user_model"](
        username=request.POST['username'],
        password_hash=make_password(request.POST['password']),
        first_name=request.POST['firstName'],
        last_name=request.POST['lastName'],
    ).save()

    return JsonResponse({'success': True})

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


@csrf_exempt
def new_order(request):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required.'
            })
    #TODO post request for a new order, update inventory - from customer
    response = JsonResponse({'Success': True})
    return response


def available_inventory(request):
    response = JsonResponse({'Status': 'unable to access database'})
    #TODO get request for things available to order (including prices) - for customer
    return response


def full_inventory(request):
    response = JsonResponse({'Status': 'unable to access database'})
    #TODO get request for what's in the inventory (including prices) - for manager
    return response
"""
    how much of each type of ice cream is left
    how much of each type of cone is left
    how much of each type of topping is left
    what the unit price of each item is
"""


def finances(request):
    response = JsonResponse({'status': 'unable to access database'})
    #TODO get request for the money spent and made - does revenue have it's own model or is it with inventory?
    return response

@csrf_exempt
def update_inventory(request):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })
    #TODO post request for update inventory - from manager
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
def new_drone(request):
    if request.method != "POST":
        return JsonResponse({
            'success': False,
            'message': 'POST method required'
        })
    #TODO post request for new drone (with what's available) **
    response = JsonResponse({'success': True})

#TODO add all the information a customer will see **
"""
    first and last name
    username
    past orders
    password?
"""

@verify_customer_token
def private_customer_data(request, user):
    return JsonResponse({"firstName": user.first_name})


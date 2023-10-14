from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import DroneStatus, Customer


def hello_world(request):
    return JsonResponse({"helloWorld": False})


def get_drone_statuses(request):
    statuses = DroneStatus.objects.all()

    statuses_arr = []
    for status in statuses:
        statuses_arr.append({
            "text": status.text
        })

    return JsonResponse({"droneStatuses": statuses_arr})


@csrf_exempt
def new_customer(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'message': 'POST method required. Do not use these credentials.'})

    # if username taken
    if Customer.objects.filter(pk=request.POST['username']):
        return JsonResponse({'success': False, 'message': 'username taken'})

    Customer(
        username=request.POST['username'],
        password_hash=make_password(request.POST['password']),
        first_name=request.POST['firstName'],
        last_name=request.POST['lastName'],
    ).save()

    return JsonResponse({'success': True})

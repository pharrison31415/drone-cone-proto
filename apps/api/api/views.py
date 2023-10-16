from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

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

def new_customer(request):
    username = request.POST['username']
    #take the password sent over, hash it, save the hash to the database
    return JsonResponse({'success': True})

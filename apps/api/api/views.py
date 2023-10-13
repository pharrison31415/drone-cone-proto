from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from api.models import DroneStatus


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

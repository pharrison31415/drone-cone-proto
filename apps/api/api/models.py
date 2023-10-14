from django.db import models as md
from datetime import datetime


class Customer(md.Model):
    username = md.CharField(primary_key=True, max_length=64)
    password_hash = md.CharField(max_length=128)
    first_name = md.CharField(max_length=64)
    last_name = md.CharField(max_length=64)
    created = md.DateTimeField(auto_now=True)


class Owner(md.Model):
    username = md.CharField(primary_key=True, max_length=64)
    password_hash = md.CharField(max_length=128)
    first_name = md.CharField(max_length=64)
    last_name = md.CharField(max_length=64)
    created = md.DateTimeField(auto_now=True)


class DroneType(md.Model):
    text = md.CharField(max_length=32)
    capacity = md.PositiveIntegerField()


class DroneStatus(md.Model):
    text = md.CharField(primary_key=True, max_length=32)


class Drone(DroneType):
    def last_use_default():
        return datetime(1970, 1, 1, 0, 0, 0, 0)

    status = md.ForeignKey(DroneStatus, on_delete=md.PROTECT)
    owner = md.ForeignKey(Owner, on_delete=md.PROTECT)
    last_use = md.DateTimeField(null=True, default=last_use_default)
    created = md.DateTimeField(auto_now=True)


class OrderStatus(md.Model):
    text = md.CharField(primary_key=True, max_length=32)


class Order(md.Model):
    customer = md.ForeignKey(Customer, on_delete=md.PROTECT)
    drone = md.ForeignKey(Drone, on_delete=md.PROTECT)
    price = md.PositiveIntegerField()
    status = md.ForeignKey(OrderStatus, on_delete=md.PROTECT)
    created = md.DateTimeField(auto_now=True)

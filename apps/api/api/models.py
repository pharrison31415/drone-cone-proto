from django.db import models as md
from datetime import datetime


class User(md.Model):
    username = md.CharField(primary_key=True, max_length=64)
    password_hash = md.CharField(max_length=128)
    first_name = md.CharField(max_length=64)
    last_name = md.CharField(max_length=64)
    created = md.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

    def toJSON(self):
        return {
            "username": self.username,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "created": self.created,
        }

class Customer(User): pass
class Manager(User): pass
class Owner(User): pass

class Token(md.Model):
    token = md.CharField(primary_key=True, max_length=128)
    created = md.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class CustomerToken(Token):
    user = md.ForeignKey(Customer, on_delete=md.PROTECT)

class ManagerToken(Token):
    user = md.ForeignKey(Manager, on_delete=md.PROTECT)

class OwnerToken(Token):
    user = md.ForeignKey(Owner, on_delete=md.PROTECT)


class InventoryItem(md.Model):
    name = md.CharField(primary_key=True, max_length=128)
    quantity = md.PositiveIntegerField(default=0)
    unit_cost = md.PositiveIntegerField()
    image_url = md.URLField()

    class Meta:
        abstract = True

    def toJSON(self):
        return {
            "name": self.name,
            "imageUrl": self.image_url,
        }

class ConeType(InventoryItem): pass
class IceCreamType(InventoryItem): pass
class ToppingType(InventoryItem): pass

class Cone(md.Model):
    cone_type = md.ForeignKey(ConeType, on_delete=md.PROTECT)
    ice_cream_type = md.ForeignKey(IceCreamType, on_delete=md.PROTECT)
    topping_type = md.ForeignKey(ToppingType, on_delete=md.PROTECT)
    created = md.DateTimeField(auto_now=True)

    def toJSON(self):
        return {
            "coneType": self.cone_type.toJSON(),
            "iceCreamType": self.ice_cream_type.toJSON(),
            "toppingType": self.topping_type.toJSON(),
            "created": self.created,
        }


class DroneType(md.Model):
    text = md.CharField(primary_key=True, max_length=32)
    capacity = md.PositiveIntegerField()

    def toJSON(self):
        return {
            "text": self.text,
            "capacity": self.capacity,
        }


class DroneStatus(md.Model):
    text = md.CharField(primary_key=True, max_length=32)

    def toJSON(self):
        return {
            "text": self.text,
        }


class Drone(md.Model):
    def last_use_default():
        return datetime(1970, 1, 1, 0, 0, 0, 0)

    status = md.ForeignKey(DroneStatus, on_delete=md.PROTECT)
    drone_type = md.ForeignKey(DroneType, on_delete=md.PROTECT)
    owner = md.ForeignKey(Owner, on_delete=md.PROTECT)
    last_use = md.DateTimeField(null=True, default=last_use_default)
    created = md.DateTimeField(auto_now=True)
    
    def toJSON(self):
        return {
            "status": self.status.toJSON(),
            "droneType": self.drone_type.toJSON(),
            "owner": self.owner.toJSON(),
            "lastUse": self.last_use,
            "created": self.created,
        }


class OrderStatus(md.Model):
    text = md.CharField(primary_key=True, max_length=32)

    def toJSON(self):
        return {
            "text": self.text
        }


class Order(md.Model):
    customer = md.ForeignKey(Customer, on_delete=md.PROTECT)
    cone = md.ForeignKey(Cone, on_delete=md.PROTECT)
    drone = md.ForeignKey(Drone, on_delete=md.PROTECT)
    price = md.PositiveIntegerField()
    status = md.ForeignKey(OrderStatus, on_delete=md.PROTECT)
    created = md.DateTimeField(auto_now=True)

    def toJSON(self):
        return {
            "customer": self.customer.toJSON(),
            "cone": self.cone.toJSON(),
            "drone": self.drone.toJSON(),
            "price": self.price,
            "status": self.status.toJSON(),
            "created": self.crated,
        }

class Message(md.Model):
    content = md.CharField(max_length=1024)
    handled = md.BooleanField(default=False)
    handled_by = md.ForeignKey(Manager, null=False, on_delete=md.PROTECT)
    created = md.DateTimeField(auto_now=True)

    def toJSON(self):
        return {
            "content": self.content,
            "handled": self.handled,
            "created": self.created,
        }
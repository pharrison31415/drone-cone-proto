# Generated by Django 4.2.3 on 2023-10-07 00:28

from django.db import migrations


ORDER_STATUSES = [
    {"text": "delivering"},
    {"text": "delivered"},
]


def populate(apps, schema_editor):
    OrderStatus = apps.get_model("api", "OrderStatus")

    for status in ORDER_STATUSES:
        OrderStatus(
            text=status["text"]
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_populate_DroneStatus'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]

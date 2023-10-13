# Generated by Django 4.2.3 on 2023-10-07 00:15

from django.db import migrations


DRONE_TYPES = [
    {"text": "light", "capacity": 1},
    {"text": "medium", "capacity": 4},
    {"text": "heavy", "capacity": 8},
]


def populate(apps, schema_editor):
    DroneType = apps.get_model("api", "DroneType")

    for dt in DRONE_TYPES:
        DroneType(
            text=dt["text"],
            capacity=dt["capacity"]
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]
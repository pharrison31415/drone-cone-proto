# Generated by Django 4.2.3 on 2023-10-25 17:27

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_use', models.DateTimeField(default=api.models.Drone.last_use_default, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DroneStatus',
            fields=[
                ('text', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DroneType',
            fields=[
                ('text', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('text', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OwnerToken',
            fields=[
                ('token', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.owner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.customer')),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.drone')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.orderstatus')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerToken',
            fields=[
                ('token', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.manager')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='drone',
            name='drone_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.dronetype'),
        ),
        migrations.AddField(
            model_name='drone',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.owner'),
        ),
        migrations.AddField(
            model_name='drone',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.dronestatus'),
        ),
        migrations.CreateModel(
            name='CustomerToken',
            fields=[
                ('token', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

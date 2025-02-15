# Generated by Django 5.1.6 on 2025-02-15 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxi_name', models.CharField(max_length=50)),
                ('license_plate', models.CharField(max_length=50, unique=True)),
                ('driver_name', models.CharField(max_length=100)),
                ('passenger_capacity', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)])),
                ('car_model', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Select Status', 'Select Status'), ('Available', 'Available'), ('Busy', 'Busy'), ('Under Maintenance', 'Under Maintenance')], max_length=20)),
            ],
        ),
    ]

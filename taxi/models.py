from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Taxi(models.Model):
    TAXI_CHOICES = [
        ('Select Status','Select Status'),
        ('Available','Available'),
        ('Busy','Busy'),
        ('Under Maintenance','Under Maintenance')
    ]

    taxi_name = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50, unique=True)
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.PositiveIntegerField(
        validators =  [
            MaxValueValidator(6),
            MinValueValidator(1)
        ]
    )
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=TAXI_CHOICES)

    def __str__(self):
        return self.taxi_name
from django.shortcuts import render
from .models import Taxi


def taxi_list(request):
    taxi_name = request.GET.get('taxi_name')
    license_plate = request.GET.get('license_plate')
    driver_name = request.GET.get('driver_name')
    passenger_capacity = request.GET.get('passenger_capacity')
    car_model = request.GET.get('car_model')
    status = request.GET.get('status')

    if taxi_name and license_plate and driver_name and passenger_capacity and car_model and status:
        Taxi.objects.create(
            taxi_name = taxi_name,
            license_plate = license_plate,
            driver_name = driver_name,
            passenger_capacity = passenger_capacity,
            car_model = car_model,
            status = status
        )
    taxi = Taxi.objects.all()
    ctx = {'taxi': taxi}
    return render(request, 'taxi/taxi_list.html', ctx)
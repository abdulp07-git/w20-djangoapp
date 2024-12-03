from django.shortcuts import render
from django.http import HttpResponse
from .models import car_data
from django.http import JsonResponse
import socket

# Create your views here.

def home(request):
    hostname = socket.gethostname()
    return render(request, 'home.html', {'hostname': hostname})

def gallery(request):
    return render(request, 'gallery.html')

def add(request):
    return render(request, 'addition.html')

def result(request):
    val1 = int(request.POST["val1"])
    val2 = int(request.POST["val2"])
    result = val1 + val2

    return render(request, 'result.html', {'result': result})

#def car(request):
    #data = car_data.objects.all()
    #return render(request, 'car.html', {'data': data})

def car(request):
    car_makers = car_data.objects.values('make').distinct()  # Get unique car makers
    return render(request, 'car.html', {'car_makers': car_makers})

def model(request):
    car_maker = request.GET.get('carMaker')  # Retrieve the car maker from the query parameters
    if car_maker:
        car_models = car_data.objects.filter(make=car_maker).values('model')
    else:
        car_models = []
    return render(request, 'model.html', {'car_maker': car_maker, 'car_models': car_models})


def price(request):
    car_maker = request.GET.get('carMaker')
    car_model = request.GET.get('carModel')
    car_price = None

    if car_maker and car_model:
        # Fetch the price based on car maker and model
        car = car_data.objects.filter(make=car_maker, model=car_model).first()
        if car:
            car_price = car.price  # Assuming `price` is a field in your car_data model

    return render(request, 'price.html', {
        'car_maker': car_maker,
        'car_model': car_model,
        'car_price': car_price
    })



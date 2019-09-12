from django.shortcuts import render
from .models import CarBrand


def cars(request):
	cars = CarBrand.objects.all()

	return render(request, 'cars/home.html', locals())

def ferrari(request):
	ferraries = CarBrand.objects.filter(brand='Ferrari')
	return render(request, 'cars/ferrari.html', locals())


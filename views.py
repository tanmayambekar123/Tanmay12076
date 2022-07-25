from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from mycar import models
from .models import Car,Owner,Order



def all_data(request):
    data =Order.objects.all()
    return render(request, 'mycar/car.html',locals()) 
    

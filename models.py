from operator import mod
from django.db import models

# Create your models here.

class Car(models.Model):
    model_name=models.CharField(max_length=500)
    model_num=models.CharField(max_length=30)
    prize=models.PositiveIntegerField()

    def __str__(self):
        return self.model_name;


class Owner(models.Model):
    name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=15)

    def __str__(self):
        return self.name;

class Order(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    unit = models.PositiveIntegerField() 

    def __str__(self):
        return self.owner.name + ' ' + self.car.model_name;
    
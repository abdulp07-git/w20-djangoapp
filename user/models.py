from django.db import models

# Create your models here.

class car_data(models.Model):
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    price = models.CharField(max_length=25)

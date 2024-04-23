from django.db import models

class Product(models.Model):

    name=models.CharField(default="",max_length=100)
    price=models.CharField(default="",max_length=500)

    quantity=models.CharField(default="",max_length=10)


# Create your models here.

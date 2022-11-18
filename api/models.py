from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()
    sale_price = models.IntegerField()

    def __str__(self):
        return self.name


class Users(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class ShoppingCart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Shopping(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()
    state = models.BooleanField()

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField()
    sale_price = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.description}'


class Users(AbstractUser):
    username = models.CharField(max_length = 255)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username}'


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

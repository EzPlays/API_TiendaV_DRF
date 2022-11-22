from django.contrib import admin
from api.models import Users, Products, Shopping, ShoppingCart

# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Shopping)
admin.site.register(ShoppingCart)
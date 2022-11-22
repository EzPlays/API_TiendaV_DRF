from .models import Products, Shopping, ShoppingCart, Users
from .serializer import ProductsSerializer, ShoppingCartSerializer, ShoppingSerializer, UsersSerializer
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductsSerializer


class ShoppingViewSet(viewsets.ModelViewSet):
    queryset = Shopping.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ShoppingSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ShoppingCartSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer


    
    




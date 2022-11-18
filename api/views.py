from rest_framework import viewsets, permissions
from .models import Products, Shopping, ShoppingCart, Users
from .serializer import ProductsSerializer, ShoppingCartSerializer, ShoppingSerializer, UsersSerializer, UsersLoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductsViewSet(viewsets.ModelViewSet):

    def get_queryset(self):

        products = Products.objects.all()

        name = self.request.GET.get('name')

        if name:
            products = products.filter(name__contains=name)

        return products

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

    # def get_queryset(self):

    #     login = Users.objects.all()

    #     email = self.request.GET.get('email')
    #     password = self.request.GET.get('password')

    #     if email and password:
    #         # login = login.filter(email__iexact=email, password__iexact=password)
    #         print('token')
    #     return login

    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer


class UserLoginViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersLoginSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Users.objects.all()
            x = queryset
            print(len(x))
            # a = []
            # a = list(Users.objects.all()) 
            # print(a[1])
            # for query in len(queryset):
            #     print(query.email)
                
        else:
            email =self.request.POST['email']
            password = self.request.POST['password']
            x = print(email, password)
            return Response(x)
        
    
    




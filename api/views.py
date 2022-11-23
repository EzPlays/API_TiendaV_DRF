from .models import Products, Shopping, ShoppingCart, Users
from .serializer import ProductsSerializer, ShoppingCartSerializer, ShoppingSerializer, UsersSerializer
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from api.serializer import (
    CustomTokenObtainPairSerializer, CustomUserSerializer
)
from django_filters.rest_framework import DjangoFilterBackend



class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductsSerializer


class ShoppingViewSet(viewsets.ModelViewSet):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = ShoppingSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `user` query parameter in the URL.
        """
        queryset = Shopping.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user__id = user)
        return queryset


# class ShoppingCartGetViewSet(viewsets.ModelViewSet):

#     permission_classes = [permissions.AllowAny]
#     serializer_class = ShoppingCartSerializer
#     # queryset = ShoppingCartSerializer.Meta.model.objects.filter(user__id = 14)

#     def get_queryset(self):
#         pk = self.request.query_params.get('pk')
#         if pk is not None:
#             queryset = ShoppingCartSerializer.Meta.model.objects.filter(user__id = pk)
#             return print(queryset) 

#     # def get_queryset(self):
#     #     pk = self.request.body
#     #     if pk is None:
#     #         # getCart = ShoppingCart.objects.all()
#     #         print('all')
#     #         return self.get_serializer().Meta.model.objects.all()
#     #     else:
#     #         print('filtro')
#     #         return self.get_serializer().Meta.model.objects.filter(user__id = pk).first()


#funciona 3
class ShoppingCartViewSet(viewsets.ModelViewSet):

    # queryset = ShoppingCartSerializer.Meta.model.objects.filter(user__id = 14)
    
    permission_classes = [permissions.AllowAny]
    serializer_class = ShoppingCartSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `user` query parameter in the URL.
        """
        queryset = ShoppingCart.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user__id = user)
        return queryset


# funciona 2
# class ShoppingCartViewSet(viewsets.ModelViewSet):

#     # queryset = ShoppingCartSerializer.Meta.model.objects.filter(user__id = 14)
    
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ShoppingCartSerializer
    
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         pk = self.kwargs['pk']
#         return ShoppingCartSerializer.Meta.model.objects.filter(user__id = pk)


# funciona
# class ShoppingCartViewSet(viewsets.ModelViewSet):

#     # queryset = ShoppingCartSerializer.Meta.model.objects.filter(user__id = 14)
#     queryset = ShoppingCart.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ShoppingCartSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['user', 'product']

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     print(pk)
    #     return ShoppingCartSerializer.Meta.model.objects.filter(user__id = pk)


    # def get_queryset(self):
        
    #     pk = self.kwargs['pk']
    #     print(pk)
    #     x = ShoppingCartSerializer.Meta.model.objects.filter(user__id = pk)
    #     return x
    #     # if pk is None:
    #     #     print(pk)
    #     #     return ShoppingCartSerializer.Meta.model.objects.all()
    #     # else:
    #     #     print(pk)
    #     #     x = ShoppingCartSerializer.Meta.model.objects.filter(user__id = pk)
    #     #     print(x)
    #     #     y = ShoppingCartSerializer(x)
    #     #     print(y.data)
    #     #     return 


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = authenticate(
            email=email,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o email incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o email incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = Users.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)
    
    




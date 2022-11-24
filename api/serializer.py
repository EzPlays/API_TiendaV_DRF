from rest_framework import serializers
from .models import Products, Shopping, ShoppingCart, Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','username')


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class ShoppingSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'user': instance.user.__str__(),
            'name': instance.product.name,
            'description': instance.product.description,
            'quantity': instance.quantity,
            'total': instance.total,
            'state': instance.state,
        }

    class Meta:
        model = Shopping
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'user': instance.user.__str__(),
            'id_product': instance.product.id,
            'name': instance.product.name,
            'description': instance.product.description,
            'quantity': instance.quantity,
            'sale_price': instance.product.sale_price,
        }

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        user = Users(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

    class Meta:
        model = Users
        fields = ('id','username','email','password')





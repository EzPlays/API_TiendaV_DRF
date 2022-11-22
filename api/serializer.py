from rest_framework import serializers
from .models import Products, Shopping, ShoppingCart, Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# serializers

class ProductsSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        existe = Products.objects.filter(name__iexact=value).exists()
        if existe:
            raise serializers.ValidationError('Este nombre de producto ya existe')
        return existe

    class Meta:
        model = Products
        fields = '__all__'


class ShoppingSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'user': instance.user.__str__(),
            'product': instance.product.__str__(),
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
            'product': instance.product.__str__(),
            'quantity': instance.quantity,
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





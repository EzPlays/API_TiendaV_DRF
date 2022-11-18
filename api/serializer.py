from rest_framework import serializers
from .models import Products, Shopping, ShoppingCart, Users

# serializers


class ProductsSerializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=3)

    def validate_name(self, value):
        existe = Products.objects.filter(name__iexact=value).exists()

        if existe:
            raise serializers.ValidationError(
                'este nombre de producto ya existe')
        return existe

    class Meta:
        model = Products
        fields = '__all__'


class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):

    # username = serializers.CharField(read_only=True, source='user.username')
    # product = ProductsSerializer(read_only=True)
    # product_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Products.objects.all(), source='product')

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class UsersLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['email', 'password']
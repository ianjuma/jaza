from rest_framework import serializers

from products.models import Product, Category
from authentication.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = ('category', 'id')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Product

        fields = ('id', 'name', 'created_at', 'updated_at', 'category', 'owner')

        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(ProductSerializer, self).get_validation_exlusions()

            return exclusions + ['name', 'owner']

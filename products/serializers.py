from rest_framework import serializers

from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = ('category', 'id')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, read_only=True)

    class Meta:
        model = Product

        fields = ('id', 'name', 'created_at', 'updated_at', 'category')

        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Product, self).get_validation_exlusions()

            return exclusions + ['name']

from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='product_owner')
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='product_category')

    class Meta:
        model = Product

        fields = ('id', 'name', 'created_at', 'updated_at', 'owner', 'category')

        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Product, self).get_validation_exlusions()

            return exclusions + ['name']
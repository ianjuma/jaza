from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = ('id', 'quantity', 'name', 'created_at', 'updated_at',
                  'cost_per_unit', 'percent_discount', 'units')

        # ? type - owner
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Product, self).get_validation_exlusions()

            return exclusions + ['name']
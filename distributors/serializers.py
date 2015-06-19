from rest_framework import serializers

from products.models import Account
from products.serializers import ProductSerializer


# TODO: fetch distributor products - set many=True
class DistributorSerializer(serializers.ModelSerializer):

    products = ProductSerializer(read_only=False, required=False, many=True)

    class Meta:
        model = Account

        fields = ('id', 'email', 'products', 'username', 'last_name', 'first_name',
                  'created_at', 'updated_at')
        read_only_fields = ('id',)

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(DistributorSerializer, self).get_validation_exlusions()

            return exclusions + ['id', 'user']
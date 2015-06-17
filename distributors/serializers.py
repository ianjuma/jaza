from rest_framework import serializers

from products.models import Distributor
from products.serializers import ProductSerializer
from authentication.serializers import UserSerializer


class DistributorSerializer(serializers.ModelSerializer):
    queryset = Distributor.objects.select_related()

    products = ProductSerializer(read_only=False, required=False)
    # user = serializers.PrimaryKeyRelatedField(queryset=queryset)
    user = UserSerializer(read_only=False, required=False)

    class Meta:
        model = Distributor

        fields = ('id', 'user', 'products')
        read_only_fields = ('id',)

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Distributor, self).get_validation_exlusions()

            return exclusions + ['id']
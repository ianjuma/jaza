from rest_framework import serializers

from products.models import Distributor
from products.serializers import ProductSerializer
from authentication.serializers import UserSerializer


# TODO: fetch distributor products - set many=True
class DistributorSerializer(serializers.ModelSerializer):
    # queryset = Product.objects.all()
    # products = serializers.ManyRelatedField(child_relation=user, read_only=True)

    products = ProductSerializer(read_only=False, required=False, many=True)
    user = UserSerializer(read_only=False, required=False)

    class Meta:
        model = Distributor

        fields = ('id', 'user', 'products')
        read_only_fields = ('id',)

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(DistributorSerializer, self).get_validation_exlusions()

            return exclusions + ['id']
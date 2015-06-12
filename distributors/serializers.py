from rest_framework import serializers

from products.models import Distributor


class DistributorSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Distributor

        fields = ('id', 'name', 'national_id', 'phone_number', 'date_joined',
                  'last_login', 'products', 'email')
        read_only_fields = ('id', 'last_login', 'date_joined')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Distributor, self).get_validation_exlusions()

            return exclusions + ['id', 'name']
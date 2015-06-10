from rest_framework import serializers

from products.models import Distributor


class DistributorSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Distributor

        fields = ('id', 'last_name', 'national_id', 'phone_number', 'type', 'created_at',
                  'updated_at', 'nationality', 'first_name', 'products')
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Distributor, self).get_validation_exlusions()

            return exclusions + ['first_name', 'last_name']
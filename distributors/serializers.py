from rest_framework import serializers

from distributors.models import Distributor


class DistributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distributor

        fields = ('id', 'name', 'national_id', 'phone_number', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Distributor, self).get_validation_exlusions()

            return exclusions + ['name']
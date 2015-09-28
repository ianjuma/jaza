from rest_framework import serializers

from products.models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    owner_queryset = User.objects.all()

    owner = serializers.PrimaryKeyRelatedField(queryset=owner_queryset)

    class Meta:
        model = Product

        fields = ('id', 'name', 'category', 'owner', 'created_at', 'ussd_channel')

        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(ProductSerializer, self).get_validation_exlusions()

            return exclusions + ['name', 'owner']

from rest_framework import serializers

from agents.models import Agent
from products.serializers import ProductSerializer


class AgentSerializer(serializers.ModelSerializer):

    products = ProductSerializer(read_only=False, required=False, many=True)

    class Meta:
        model = Agent

        fields = ('id', 'products', 'phone_number', 'name', 'pin')
        read_only_fields = ('id',)

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(AgentSerializer, self).get_validation_exlusions()

            return exclusions + ['id']
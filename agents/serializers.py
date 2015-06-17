from rest_framework import serializers

from agents.models import Agent
from products.serializers import ProductSerializer
from authentication.serializers import UserSerializer


class AgentSerializer(serializers.ModelSerializer):
    # queryset = Agent.objects.select_related()
    # user = serializers.PrimaryKeyRelatedField(queryset=queryset)

    user = UserSerializer(read_only=True, required=False)
    products = ProductSerializer(read_only=True, required=False, many=True)

    class Meta:
        model = Agent
        depth = 1

        fields = ('id', 'user', 'products', 'phone_number', 'national_id',)
        read_only_fields = ('id',)

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(AgentSerializer, self).get_validation_exlusions()

            return exclusions + ['id']
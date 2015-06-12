from rest_framework import serializers

from agents.models import Agent
from products.serializers import ProductSerializer


class AgentSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # ? -- add serializer directly or use a relation -- and depth
    # queryset - for primary key related
    # DialPlan.object.select_related.all()
    products = ProductSerializer(source='products')

    class Meta:
        model = Agent
        depth = 1

        fields = ('id', 'name', 'national_id', 'phone_number', 'email', 'products')
        read_only_fields = ('id', 'last_login', 'date_joined')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Agent, self).get_validation_exlusions()

            return exclusions + ['name']

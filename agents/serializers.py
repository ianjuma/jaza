from rest_framework import serializers

from agents.models import Agent
from products.serializers import ProductSerializer


# TODO: HyperLinkRelatedField
class AgentSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # ? -- add serializer directly or use a relation -- and depth
    # queryset - for primary key related
    # DialPlan.object.select_related.all()
    products = ProductSerializer(source='products')

    class Meta:
        model = Agent
        depth = 1

        fields = ('id', 'first_name', 'last_name', 'national_id', 'phone_number', 'created_at',
                  'updated_at', 'email', 'nationality', 'type', 'products')
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Agent, self).get_validation_exlusions()

            return exclusions + ['name']

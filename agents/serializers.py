from rest_framework import serializers

from agents.models import Agent


# TODO: HyperLinkRelatedField
class AgentSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Agent

        fields = ('id', 'first_name', 'last_name', 'national_id', 'phone_number', 'created_at',
                  'updated_at', 'email', 'nationality', 'type', 'products')
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Agent, self).get_validation_exlusions()

            return exclusions + ['name']
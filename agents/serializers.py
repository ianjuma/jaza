from rest_framework import serializers

from agents.models import Agent


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent

        fields = ('id', 'name', 'national_id', 'phone_number', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exlusions(self, *args, **kwargs):
            exclusions = super(Agent, self).get_validation_exlusions()

            return exclusions + ['name']
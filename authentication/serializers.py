from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at', 'first_name',
                  'last_name', 'tagline', 'password', 'confirm_password')

        read_only_fields = ('created_at', 'updated_at')

        @staticmethod
        def create(validated_data):
            return Account.objects.create_user(**validated_data)
            # passing a dict using **kwargs

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.tagline = validated_data.get('tagline', instance.tagline)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            # TODO: too many negatives :( de-morgans law
            if password and confirm_password and password == confirm_password:
                    instance.set_password(password)
                    instance.save()

            update_session_auth_hash(self.context.get('request'), instance)
            return instance
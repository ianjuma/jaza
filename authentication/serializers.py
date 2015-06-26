from django.contrib.auth import update_session_auth_hash
from products.models import Distributor
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Distributor
        fields = ('id', 'email', 'last_name', 'first_name', 'password',
                  'confirm_password', 'email', 'username', 'created_at', 'updated_at')
        read_only_fields = ('updated_at', 'created_at', 'id')

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()
            else:
                raise serializers.ValidationError("Passwords do not match")

            update_session_auth_hash(self.context.get('request'), instance)
            return instance
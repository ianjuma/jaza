from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'email', 'date_joined', 'last_login', 'password',
                  'confirm_password', 'phone_number')
        read_only_fields = ('date_joined', 'last_login', 'id')

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

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
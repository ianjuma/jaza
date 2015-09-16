from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'last_name', 'first_name', 'password', 'username', 'last_login', 'is_active')
        read_only_fields = ('id', 'is_active')
        write_only_fields = ('password', 'last_login')

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
                print password
            instance.save()
            return instance

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.email)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.first_name = validated_data.get('first_name', instance.first_name)

            instance.save()
            password = validated_data.get('password', None)

            if password is not None:
                instance.set_password(password)

            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)
            return instance
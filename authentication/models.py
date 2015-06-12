from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **kwargs):
        if not kwargs.get('name'):
            raise ValueError('Users must have a valid name.')

        if not phone_number:
            raise ValueError('Users must have a valid phone_number.')

        account = self.model(
            name=kwargs.get('first_name'),
            phone_number=phone_number
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, phone_number, password, **kwargs):
        account = self.create_user(phone_number, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(User):
    phone_number = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=40, blank=True)
    objects = AccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'phone_number']

    def __unicode__(self):
        return self.phone_number

    def get_full_name(self):
        return ':'.join([self.name, self.phone_number])

    def get_short_name(self):
        return self.name

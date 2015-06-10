from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **kwargs):
        if not kwargs.get('first_name'):
            raise ValueError('Users must have a valid first name.')

        if not kwargs.get('last_name'):
            raise ValueError('Users must have a valid last name.')

        if not phone_number:
            raise ValueError('Users must have a valid phone_number.')

        account = self.model(
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('first_name'),
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


class Account(AbstractBaseUser):
    USER_TYPE = (
        ('A', 'AGENT'),
        ('D', 'DISTRIBUTOR')
    )
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    type = models.CharField(max_length=1, blank=False, choices=USER_TYPE)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __unicode__(self):
        return self.phone_number

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
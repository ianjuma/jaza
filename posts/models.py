from django.db import models
from authentication.models import Account


class Users(models.Model):
    id = models.ForeignKey(Account)
    name = models.CharField(max_length=100, required=True)
    national_id = models.CharField(max_length=20, required=True, unique=True)
    _type = models.IntegerField(max_length=1, required=True)
    phone_number = models.CharField(max_length=15, required=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)
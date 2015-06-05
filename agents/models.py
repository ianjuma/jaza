from django.db import models
from products.models import Product
from authentication.models import Account


class Agent(models.Model, Account):
    # id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Product)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nationality = models.CharField(max_length=20)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.name)
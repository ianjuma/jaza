from django.db import models
from products.models import Product
from authentication.models import Account


class Agent(Account):
    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Product)
    nationality = models.CharField(max_length=20)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.name)
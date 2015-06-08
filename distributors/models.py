from django.db import models
from products.models import Product
from authentication.models import Account


class Distributor(Account):
    national_id = models.IntegerField(unique=True)
    products = models.ManyToManyField(Product)
    nationality = models.CharField(max_length=20)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.name)

from django.db import models
from authentication.models import Account


class Product(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )

    category = models.CharField(max_length=1, choices=CATEGORIES)
    name = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.name)


# TODO: fix cyclic dependency problem
class Distributor(Account):
    national_id = models.IntegerField(unique=True)
    products = models.ManyToManyField(Product, through='DistributorProductRelationship', null=False)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.phone_number)


class DistributorProductRelationship(models.Model):
    product_id = models.ForeignKey(Product, null=False)
    distributor_id = models.ForeignKey(Distributor, null=False)

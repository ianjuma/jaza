from django.db import models
from authentication.models import Account


class Product(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )

    category = models.CharField(max_length=1, choices=CATEGORIES)
    owner = models.ForeignKey('Distributor', related_name='dist_product_rel')
    name = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.name)


class Distributor(models.Model):
    id = models.OneToOneField(Account, unique=True, related_name='distributor_id', primary_key=True)
    national_id = models.IntegerField(unique=True)
    products = models.ManyToManyField(Product, through='DistributorProductRelationship', null=False)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.national_id)


class DistributorProductRelationship(models.Model):
    product_id = models.ForeignKey(Product, null=False)
    distributor_id = models.ForeignKey(Distributor, null=False)

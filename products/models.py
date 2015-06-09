from django.db import models
# from distributors.models import Distributor
from authentication.models import Account


class Category(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    TRACKING = (
        ('1', 'Tracked'),
        ('0', 'NOT TRACKED')
    )
    tracking = models.CharField(max_length=1, choices=TRACKING)
    category = models.CharField(max_length=1, choices=CATEGORIES)
    owner = models.ForeignKey('Distributor')
    # ?
    # type = models.CharField(max_length=1, choices=CATEGORIES)
    # product_id - dist_id
    # through another table - ManyToMany


class Product(models.Model):
    """
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    """
    # id = models.AutoField(primary_key=True, auto_created=True

    # owner = models.ForeignKey('Distributor')
    category = models.ForeignKey('Category')  # many to one rel ? wtf
    name = models.CharField(max_length=50, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    units = models.CharField(max_length=20)
    cost_per_unit = models.PositiveIntegerField(blank=False, default=1)
    percent_discount = models.PositiveIntegerField(default=4, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.name)


# TODO: fix cyclic dependency problem
class Distributor(Account):
    national_id = models.IntegerField(unique=True)
    products = models.ManyToManyField(Product, through='ProductDistributorRelationship')
    nationality = models.CharField(max_length=20)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.name)


class ProductDistributorRelationship(models.Model):
    product_id = models.ForeignKey(Product)
    distributor_id = models.ForeignKey(Distributor)
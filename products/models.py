from django.db import models
from authentication.models import Account


class Category(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    category = models.CharField(max_length=1, choices=CATEGORIES)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "categories"

    def __unicode__(self):
        return '{0}'.format(self.category)


class Product(models.Model):
    # owner = models.ForeignKey('Distributor', related_name='product_owner')
    category_id = models.ForeignKey('Category', related_name='product_category')
    name = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.name)


class Distributor(models.Model):
    id = models.OneToOneField(Account, unique=True, related_name='distributor_id', primary_key=True)
    national_id = models.IntegerField(unique=True)
    products = models.ManyToManyField(Product, through='DistributorProduct', null=False)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.national_id)


class DistributorProduct(models.Model):
    product_id = models.ForeignKey(Product, related_name='owner_id', null=False)
    distributor_id = models.ForeignKey(Distributor, related_name='dist_id', null=False)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.distributor_id)

from django.db import models
from django.contrib.auth.models import User


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
    # owner = models.ForeignKey(User, related_name='product_owner')
    category_id = models.ForeignKey('Category', related_name='product_category')
    name = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.id)


class Distributor(models.Model):
    user = models.ForeignKey(User, related_name='distributor_id')

    products = models.ManyToManyField(Product, through='ProductChannels', null=False)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.id)


class ProductChannels(models.Model):
    product_id = models.ForeignKey(Product, related_name='owner_id', null=False)
    distributor_id = models.ForeignKey(Distributor, related_name='dist_id', null=False)

    class Meta:
        ordering = ('distributor_id',)

    def __unicode__(self):
        return '{0}'.format(self.distributor_id)

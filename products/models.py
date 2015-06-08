from django.db import models
from distributors.models import Distributor


class Category(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    category = models.CharField(max_length=1, choices=CATEGORIES)
    # product_id = models.OneToOneRel(Product, to=Product, field_name='product_id')


class Product(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    # id = models.AutoField(primary_key=True, auto_created=True)
    owner = models.ForeignKey(Distributor)
    # type = models.CharField(max_length=1, choices=CATEGORIES)
    category = models.ForeignKey(Category)  # many to one rel
    name = models.CharField(max_length=50, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    units = models.CharField(max_length=20)
    cost_per_unit = models.PositiveIntegerField(blank=False, default=1)
    percent_discount = models.PositiveIntegerField(default=4, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.name)
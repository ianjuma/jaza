from django.db import models
from products.models import Product


class Agent(models.Model):
    name = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=32, unique=True)
    pin = models.CharField(max_length=64, blank=False)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.name)

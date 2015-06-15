from django.db import models
from products.models import Product
from authentication.models import Account


class Agent(models.Model):
    id = models.OneToOneField(Account, unique=True, primary_key=True)

    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Product, through='ProductChannels')

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.national_id)


class ProductChannels(models.Model):
    product_id = models.ForeignKey(Product, null=False)
    agent_id = models.ForeignKey(Agent, null=False)

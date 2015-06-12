from django.db import models
from products.models import Product
from products.models import Distributor
from authentication.models import Account


class Agent(models.Model):
    id = models.OneToOneField(Account, unique=True, related_name='agent_id', primary_key=True)

    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Distributor, through='AgentProductRelationship')

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.national_id)


class AgentProductRelationship(models.Model):
    distributor_id = models.ForeignKey(Distributor, null=False)
    product_id = models.ForeignKey(Product, null=False)
    agent_id = models.ForeignKey(Agent, null=False)

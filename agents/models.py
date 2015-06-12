from django.db import models
from products.models import Product
from products.models import Distributor
from authentication.models import Account


class Agent(Account):
    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Distributor, through='AgentProductRelationship')

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.phone_number)


class AgentProductRelationship(models.Model):
    distributor_id = models.ForeignKey(Distributor, null=False)
    product_id = models.ForeignKey(Product, null=False)
    agent_id = models.ForeignKey(Agent, null=False)

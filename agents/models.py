from django.db import models
from products.models import Product
from products.models import Distributor
from authentication.models import Account


class Agent(Account):
    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Distributor, through='AgentProductRelationship')

    # products = models.ManyToManyField(Distributor, through=Product)  # agent-distributor-product
    nationality = models.CharField(max_length=20)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.phone_number)


class AgentProductRelationship(models.Model):
    distributor_id = models.ForeignKey(Distributor, null=False)
    product_id = models.ForeignKey(Product, null=False)
    agent_id = models.ForeignKey(Agent, null=False)

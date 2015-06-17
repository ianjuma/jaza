from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.ForeignKey(User)

    phone_number = models.CharField(max_length=12, unique=True)
    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Product, through='AgentProductRelationship')

    class Meta:
        ordering = ('national_id',)

    def __unicode__(self):
        return '{0}'.format(self.national_id)


class AgentProductRelationship(models.Model):
    product_id = models.ForeignKey(Product, null=False)
    agent_id = models.ForeignKey(Agent, null=False)

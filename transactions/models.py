from django.db import models
from agents.models import Agent
from products.models import Product
from products.models import Distributor


class Transaction(models.Model):
    distributor_id = models.ForeignKey(Distributor)
    agent_id = models.ForeignKey(Agent)
    product_id = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(blank=False)
    price_per_unit = models.PositiveIntegerField(blank=False, default=1)
    percent_discount = models.PositiveIntegerField(default=4, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.id)

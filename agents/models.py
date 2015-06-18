from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.ForeignKey(User)

    phone_number = models.CharField(max_length=12, unique=True)
    national_id = models.PositiveIntegerField(unique=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ('national_id',)

    def __unicode__(self):
        return '{0}'.format(self.user.username)

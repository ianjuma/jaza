from django.db import models
from products.models import Product


class Agent(models.Model):
    STATUS = (
        ('V', 'VERIFIED'),
        ('N', 'NOT_VERIFIED')
    )
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16, unique=True)
    pin = models.CharField(max_length=64, default=None)
    verification_code = models.IntegerField(blank=False)
    verification_status = models.CharField(choices=STATUS, default='N', max_length=1)

    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.name)

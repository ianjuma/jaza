from django.db import models
from distributors.models import Distributor


# distributors are users
class Product(models.Model):
    CATEGORIES = (
        ('E', 'Airtime Voucher'),
        ('P', 'Pinless Airtime'),
    )
    owner = models.ForeignKey(Distributor, related_name='product_owner')
    category = models.CharField(max_length=1, choices=CATEGORIES)
    name = models.CharField(max_length=50, blank=False)
    ussd_channel = models.CharField(max_length=10, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.name)

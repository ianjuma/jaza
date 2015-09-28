from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Distributors are users, inheriting the django auth user model
    """
    CATEGORIES = (
        ('E', 'Airtime Voucher'),
        ('P', 'Pinless Airtime'),
    )
    owner = models.ForeignKey(User, related_name='product_owner')
    category = models.CharField(max_length=1, choices=CATEGORIES)
    name = models.CharField(max_length=50, blank=False)
    ussd_channel = models.CharField(max_length=10, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.name)

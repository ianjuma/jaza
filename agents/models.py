from django.db import models
from products.models import Product
from django.core.validators import RegexValidator


class Agent(models.Model):
    name = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=16, unique=True, validators=[RegexValidator(
        regex=r'^\+?254?\d{9,16}$', message="""Phone number must be entered in
        the format: '+254XXXXXXXXX'. Up to 16 digits allowed."""
    )])
    pin = models.CharField(max_length=64, blank=False)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return '{0}'.format(self.name)

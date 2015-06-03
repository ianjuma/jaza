from django.db import models
from distributors.models import Distributor


class Product(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    # owner = models.ForeignKey(Distributor)
    id = models.AutoField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=50, choices=CATEGORIES)
    name = models.CharField(max_length=50, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)
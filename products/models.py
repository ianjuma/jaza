from django.db import models


class Product(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    id = models.AutoField(primary_key=True, auto_created=True)
    type = models.CharField(max_length=50, choices=CATEGORIES)
    name = models.CharField(max_length=50, blank=False)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)
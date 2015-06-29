from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from authentication.models import DistributorManager


class Category(models.Model):
    CATEGORIES = (
        ('E', 'Airtime'),
        ('G', 'General')
    )
    category = models.CharField(max_length=1, choices=CATEGORIES)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "categories"

    def __unicode__(self):
        return '{0}'.format(self.category)


# distributors are users
class Product(models.Model):
    owner = models.ForeignKey('Distributor', related_name='product_owner')
    category = models.ForeignKey('Category', related_name='product_category')
    name = models.CharField(max_length=50, blank=False)
    ussd_channel = models.CharField(max_length=10, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __unicode__(self):
        return '{0}'.format(self.name)


class Distributor(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    products = models.ManyToManyField('Product', blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DistributorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = "distributors"

    def __unicode__(self):
        return self.username

    def get_username(self):
        super(Distributor, self).get_username()

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

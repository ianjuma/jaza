from django.contrib import admin
from products.models import Distributor

admin.site.register(Distributor, admin.ModelAdmin)

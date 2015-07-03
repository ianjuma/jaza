from django.contrib import admin
from products.models import Product, Distributor

admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Distributor, admin.ModelAdmin)

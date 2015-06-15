from django.contrib import admin
from products.models import Product, Category

admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)

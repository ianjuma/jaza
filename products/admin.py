from django.contrib import admin
from products.models import Product, Category, Account

admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Account, admin.ModelAdmin)

from django.contrib import admin
from distributors.models import Distributor

admin.site.register(Distributor, admin.ModelAdmin)

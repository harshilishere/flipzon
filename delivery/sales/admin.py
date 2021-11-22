from django.contrib import admin
from .models import inventory
from sales.models import newsale
# Register your models here.

admin.site.register(newsale)
admin.site.register(inventory)
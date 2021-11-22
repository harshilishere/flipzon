from django.contrib import admin
from .models import Student, inventory
from sales.models import newsale
# Register your models here.
admin.site.register(Student)
admin.site.register(newsale)
admin.site.register(inventory)
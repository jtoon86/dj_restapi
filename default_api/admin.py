from django.contrib import admin

# Register your models here.
from default_api.models import Order, Line

admin.site.register(Order)
admin.site.register(Line)

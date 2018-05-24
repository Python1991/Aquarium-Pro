from django.contrib import admin
from .models import Shipping
# Register your models here.
@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    pass
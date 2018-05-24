from django.contrib import admin
from .models import Store

# # Register your models here.
# class ProductInline(admin.TabularInline):
#     model = Product
#     extra = 1

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name')
    # inlines = (ProductInline,)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'sub_category', 'quantity', 'price',)


# class StoreAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'name', 'tel', 'notes',)
#     inlines = (ProductInline,)
from django.contrib import admin
from .models import ProductAquaticPlantPackage, ProductAquaticPlant
# Register your models here.
class ProductAquaticPlantAdminInline(admin.TabularInline):
    model = ProductAquaticPlant
    extra = 1

@admin.register(ProductAquaticPlantPackage)
class ProductAquaticPlantPackageAdmin(admin.ModelAdmin):
    inlines = (ProductAquaticPlantAdminInline,)
    list_display = ('id', 'name')
    pass

@admin.register(ProductAquaticPlant)
class ProductAquaticPlantAdmin(admin.ModelAdmin):
    filter_horizontal = ('image',)
    pass
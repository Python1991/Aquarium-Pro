from django.contrib import admin
from .models import AquaticPlant, LandscapePosition, GeneralClassification
# Register your models here.

# class LandscapePositionAdminInline(admin.TabularInline):
#     model = LandscapePosition
#     extra = 1

class AquaticPlantAdminInline(admin.TabularInline):
    model = AquaticPlant

@admin.register(AquaticPlant)
class AquaticPlantAdmin(admin.ModelAdmin):
    pass

@admin.register(LandscapePosition)
class LandscapePositionAdmin(admin.ModelAdmin):
    pass

@admin.register(GeneralClassification)
class GeneralClassificationAdmin(admin.ModelAdmin):
    inlines = (AquaticPlantAdminInline,)
    pass
from django.contrib import admin
from .models import Image, ImageSource
# Register your models here.

class ImageAdminInline(admin.TabularInline):
    model = Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ImageSource)
class ImageSourceAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline,)
    pass
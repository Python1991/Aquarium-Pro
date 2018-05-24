from django.contrib import admin
from .models import StoreEveluation, PAPPEveluation
# Register your models here.
@admin.register(StoreEveluation)
class StoreEveluationAdmin(admin.ModelAdmin):
    pass

@admin.register(PAPPEveluation)
class PAPPEveluationAdmin(admin.ModelAdmin):
    pass
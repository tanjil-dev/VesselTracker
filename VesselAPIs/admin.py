from django.contrib import admin

from .models import *

admin.site.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    search_fields = ('name', 'owner_id')

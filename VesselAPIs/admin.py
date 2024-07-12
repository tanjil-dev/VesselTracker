from django.contrib import admin
from VesselAPIs.models import Vessel, Voyage
from user.models import Parcel

admin.site.register(Vessel)
admin.site.register(Voyage)
admin.site.register(Parcel)
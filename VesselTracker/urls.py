from django.contrib import admin
from django.urls import path, include
from VesselAPIs.views import index

urlpatterns = [
    path('api/v1/', include('VesselAPIs.urls')),
    path('admin/', admin.site.urls),
    path("", index, name="index"),
]

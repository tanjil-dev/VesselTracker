from django.urls import path
from VesselAPIs.views import *

urlpatterns = [
    path('vessel/<int:pk>/', VesselDetail.as_view(), name='vessel-list-update-delete'),
    path('vessel/', VesselList.as_view(), name='vessel-list-create'),
    path('voyage/<int:pk>/', VoyageDetail.as_view(), name='voyage-list-update-delete'),
    path('voyage/', VoyagelList.as_view(), name='voyage-list-create'),
    path('upload-excel-data/', data_upload, name='upload-excel-data'),
]
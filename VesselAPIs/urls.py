from django.urls import path
from VesselAPIs.views import *

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('upload-excel-data/', data_upload, name='upload-excel-data')
]
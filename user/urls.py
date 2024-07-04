from django.urls import path
from user.views import *

urlpatterns = [
    path('', Home, name='home'),
]
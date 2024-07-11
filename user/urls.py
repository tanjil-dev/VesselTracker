from django.urls import path
from user.views import *

urlpatterns = [
    path('', Home, name='home'),
    path('vessel/', VesselView, name='vessel'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('logout/', LogoutUser, name='logout'),
]
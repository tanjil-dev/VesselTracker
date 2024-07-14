from django.urls import path
from user.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('vessel/', VesselView.as_view(), name='vessel'),
    path('profile/', profile, name='profile'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('logout/', LogoutUser, name='logout'),
]
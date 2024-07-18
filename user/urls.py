from django.urls import path
from user.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('voyage/', VoyageListView.as_view(), name='voyage'),
    path('vessel/', VesselListView.as_view(), name='vessel'),
    path('profile/', profile, name='profile'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('logout/', LogoutUser, name='logout'),
]
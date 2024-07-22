from django.urls import path
from user.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('voyage/', VoyageListView.as_view(), name='voyage'),
    path('voyage/<int:pk>/', VoyageDetailView.as_view(), name='voyage-detail'),
    path('vessel/', VesselListView.as_view(), name='vessel'),
    path('vessel/<int:pk>/', VesselDetailView.as_view(), name='vessel-detail'),
    path('parcel/', ParcelListView.as_view(), name='parcel'),
    path('parcel/<int:pk>/', ParcelDetailView.as_view(), name='parcel-detail'),
    path('profile/', profile, name='profile'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('logout/', LogoutUser, name='logout'),
]

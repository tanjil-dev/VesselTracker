from django.contrib.auth import views
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
    path('change_password/', changePassword, name='change_password'),
    path('password_reset/', views.PasswordResetView.as_view(template_name="auth/password_reset.html"), name='password_reset'),
    path('password_reset_email_sent/', views.PasswordResetDoneView.as_view(template_name="auth/password_reset_email_sent.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_done.html"), name='password_reset_complete'),
]

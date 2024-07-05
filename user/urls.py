from django.urls import path
from user.views import *

urlpatterns = [
    path('', Home, name='home'),
    path('login/', Login, name='login'),
    path('signup/', Signup, name='signup'),
    path('logout/', LogoutUser, name='logout'),
]
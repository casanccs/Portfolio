from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('createProfile/', createProfile, name='createProfile'),
]



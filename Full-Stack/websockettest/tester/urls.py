from django.urls import path

from .views import *


urlpatterns = [
    path("chat/<str:room_id>", chat, name="chat"),
    path("", home, name='home'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('createAccount/', CreateAccount, name='createAccount'),
]
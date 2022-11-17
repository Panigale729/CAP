from django.urls import path
from . import views

urlpatterns = [
     path("room/", views.room, name="room"),
     path("login/", views.loginPage, name="login"),
     path("logout/", views.logoutUser, name="logout"),
     path("register/", views.register, name="register"),
 ]
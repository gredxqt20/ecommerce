from django.urls import path
from . import views

from store.controller import authview

urlpatterns = [
    path('home', views.home, name="home"),
    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logout, name="logout"),
]

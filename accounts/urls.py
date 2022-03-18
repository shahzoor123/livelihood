from django.urls import path

from . import views

urlpatterns = [
    path('logout', views.logout, name='logout'),
    path('login', views.logedin, name='logedin'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),

]
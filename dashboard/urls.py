from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('contactus/', views.contactus, name='contactus'),
    path('search/', views.search, name='search'),
    path('calender/', views.calender, name='calender'),
    path('chart/', views.chart, name='chart'),
    path('maps/', views.maps, name='maps'),
    path('test/', views.test, name='test'),

]

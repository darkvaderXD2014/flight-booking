from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('flights/', views.flights, name='flights'),
    path('hotels/', views.hotels, name='hotels'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('schedules/', views.schedules, name='schedules'),
    path('checkout/', views.checkout, name='checkout'),
    path('del_flights/<int:pk>', views.del_flights, name='del_flights'),
    path('del_resto/<int:pk>', views.del_resto, name='del_resto'),
    path('del_hotels/<int:pk>', views.del_hotels, name='del_hotels'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('flights/', views.flights, name='flights'),
    path('hotels/', views.hotels, name='hotels'),
    path('restaurant/', views.resto, name='restaurant'),
]
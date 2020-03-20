from django.urls import path, re_path
from . import views
from plan import views as plan_views

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
    path('add_flight_plan/<int:pk>', plan_views.add_flight_plan, name='add_flight_plan')

]

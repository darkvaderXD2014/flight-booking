from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan, name='plan'),
    path('addresto', views.addresto, name='addresto'),
    path('addhotel', views.addhotel, name='addhotel'),
    path('addflights', views.addflights, name='addflights'),
]
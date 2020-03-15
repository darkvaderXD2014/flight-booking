from django.urls import path
from . import views

urlpatterns = [
	path('', views.addplan, name='addplan'),
]
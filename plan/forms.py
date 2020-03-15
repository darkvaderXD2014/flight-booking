from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Flights, RestoAndHotels

class RestoAndHotelsForm(ModelForm):
	class Meta:
		model = RestoAndHotels
		fields = ['name', 'desc', 'address', 'imageFile', 'price']

class FlightsForm(ModelForm):
	class Meta:
		model = Flights
		fields = ['name', 'desc', 'dest', 'imageFile', 'price']
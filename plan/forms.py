from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Flights, Resto, Hotels

class RestoForm(ModelForm):
	class Meta:
		model = Resto
		fields = ['name', 'desc', 'address', 'imageFile', 'price']

class HotelsForm(ModelForm):
	class Meta:
		model = Hotels
		fields = ['name', 'desc', 'address', 'imageFile', 'price']

class FlightsForm(ModelForm):
	class Meta:
		model = Flights
		fields = ['name', 'desc', 'dest', 'imageFile', 'price']
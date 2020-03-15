from django.forms import ModelForm
from .models import (Profile, Flights, Restaurant, Hotels)


class ProfileCreate(ModelForm):
	class Meta:
		model = Profile
		fields = ['flights' , 'hotels', 'restaurant']
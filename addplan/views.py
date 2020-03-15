from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import (Profile, Flights, Restaurant, Hotels)
from .forms import ProfileCreate


# Create your views here.
@login_required(login_url='/')
def addplan(request):
	form = ProfileCreate()
	if request.method == "POST":
		if form.is_valid():
			form.save()
			
	context = {
		'form' : form
	}
	return render(request, 'addplan.html', context)
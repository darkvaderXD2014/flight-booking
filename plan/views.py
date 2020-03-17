from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from .models import Resto, Hotels, Flights, Booker
from .forms import RestoForm, HotelsForm,FlightsForm
from . import models
# Create your views here.

def flight_list(request):
	context = {}
	return render(request, 'flights.html', context)

def add_flight_to_user(request, flightId):
	pass

def plan(request):
    context = {}
    return render(request, 'addplan.html', context)


# Admin Side
@staff_member_required(login_url='/')
def addhotel(request):
	if request.method == 'POST':
		form = HotelsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('hotels')
	else:
		form = HotelsForm()

	context = {
		'form' : form
	}
	return render(request, 'addhotel.html', context)

@staff_member_required(login_url='/')
def addresto(request):
	if request.method == 'POST':
		form = RestoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('restaurant')
	else:
		form = RestoForm()

	context = {
		'form' : form
	}
	return render(request, 'addresto.html', context)

@staff_member_required(login_url='/')
def addflights(request):
	if request.method == 'POST':
		form = FlightsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('flights')
		else:
			print('Error..')
	else:
		form = FlightsForm()
		
	context = {
		'form' : form
	}
	return render(request, 'addflights.html', context)


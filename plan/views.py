from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from .models import Resto, Hotels, Flights, Booker, Planner, PlannedFlights
from .forms import RestoForm, HotelsForm,FlightsForm,AddFlightsForm
from . import models
# Create your views here.

def flight_list(request):
	context = {}
	return render(request, 'flights.html', context)

def add_flight_plan(request, pk):
	flight_item = Flights.objects.get(id=pk)

	if request.method == "POST":
		form = AddFlightsForm(request.POST)
		if form.is_valid():
			description = form.cleaned_data['flights_desc']
			start_date = form.cleaned_data['flights_start']
			end_date = form.cleaned_data['flights_end']
			if not flight_item in PlannedFlights.objects.all():
				planned_fl = PlannedFlights(user=request.user)
				planned_fl.save()
				planned_fl.items.add(flight_item)	
			

			print(description)
			print(start_date)
			planned_fl.desc = description
			planned_fl.start_date = start_date
			planned_fl.end_date = end_date
			planned_fl.planned = True

			planned_fl.save()
			return redirect('home')
		else:
			print(form.errors)
	else:
		form = AddFlightsForm()

	context={
		'form': AddFlightsForm(),
		'flight' : flight_item.name
	}
	return render(request, 'add_flight_plan.html', context)

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


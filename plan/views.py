from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from .models import RestoAndHotels, Flights, Booker
from .forms import RestoAndHotelsForm,FlightsForm
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
		form = RestoAndHotelsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('flights')
	else:
		form = RestoAndHotelsForm()

	context = {
		'form' : form
	}
	return render(request, 'addhotel.html', context)

@staff_member_required(login_url='/')
def addresto(request):
	if request.method == 'POST':
		form = RestoAndHotelsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('flights')
	else:
		form = RestoAndHotelsForm()

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
		form = FlightsForm()
		
	context = {
		'form' : form
	}
	return render(request, 'addflights.html', context)


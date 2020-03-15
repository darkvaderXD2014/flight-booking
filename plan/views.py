from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .models import RestoAndHotels, Flights
from .forms import RestoAndHotelsForm,FlightsForm
# Create your views here.

@staff_member_required(login_url='/')
def addhotel(request):
	form = RestoAndHotelsForm()
	if request.method == 'POST':
		form = RestoAndHotelsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	context = {
		'form' : form
	}
	return render(request, 'addhotel.html', context)

@staff_member_required(login_url='/')
def addresto(request):
	form = RestoAndHotelsForm()
	if request.method == 'POST':
		form = RestoAndHotelsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	context = {
		'form' : form
	}
	return render(request, 'addresto.html', context)

@staff_member_required(login_url='/')
def addflights(request):
	form = RestoAndHotelsForm()
	if request.method == 'POST':
		form = FlightsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	context = {
		'form' : form
	}
	return render(request, 'addflights.html', context)

def plan(request):
    context = {}
    return render(request, 'addplan.html', context)
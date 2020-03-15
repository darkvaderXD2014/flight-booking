from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import EditProfileForm
from plan.models import Booker, Flights

@login_required(login_url='/')
def checkout(request):
    return render(request, "checkout.html", {})


@login_required(login_url='/')
def schedules(request):
    return render(request, "schedules.html", {})


@login_required(login_url='/')
def resto(request):
    return render(request, "restaurant.html", {})


@login_required(login_url='/')
def hotels(request):
    return render(request, "hotels.html", {})


@login_required(login_url='/')
def flights(request):
    context = {
        'flights' : Flights.objects.all()
    }
    return render(request, "flights.html", context)


@login_required(login_url='/')
def home(request):
    return render(request, "home.html", {})


@login_required(login_url='/')
def profile(request):
    return render(request, "profile.html", {})


@login_required(login_url='/')
def settings(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updates has been successful.')
            return redirect('settings')

    else:
        form = EditProfileForm(request.POST, instance=request.user)

    context = {'form': form}
    return render(request, 'settings.html', context)

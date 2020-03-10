from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .forms import EditProfileForm


@login_required(login_url='/')
def home(request):
    return render(request, "home.html", {})

@login_required(login_url='/')
def settings(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = EditProfileForm(request.POST, instance=request.user)
        args = {'form':form}
        return render(request, 'settings.html', args)
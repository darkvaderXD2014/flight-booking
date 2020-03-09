from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html', {})

def reg(request):
    return render(request, 'reg.html', {})
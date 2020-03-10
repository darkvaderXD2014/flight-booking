from django.shortcuts import render

# Create your views here.
def schedules(request):
    return render(request, 'schedules.html', {})
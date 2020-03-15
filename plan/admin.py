from django.contrib import admin
from .models import RestoAndHotels, Flights, Booker, Planner, PlannedFlights
# Register your models here.
admin.site.register(RestoAndHotels)
admin.site.register(Flights)
admin.site.register(Booker)
admin.site.register(Planner)
admin.site.register(PlannedFlights)
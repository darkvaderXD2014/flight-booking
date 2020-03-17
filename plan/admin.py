from django.contrib import admin
from .models import Resto, Hotels, Flights, Booker, Planner, PlannedFlights
# Register your models here.
admin.site.register(Resto)
admin.site.register(Hotels)
admin.site.register(Flights)
admin.site.register(Booker)
admin.site.register(Planner)
admin.site.register(PlannedFlights)
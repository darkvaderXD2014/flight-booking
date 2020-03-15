from django.contrib import admin
from .models import Profile, Flights, Restaurant, Hotels
# Register your models here.

admin.site.register(Profile)
admin.site.register(Flights)
admin.site.register(Restaurant)
admin.site.register(Hotels)

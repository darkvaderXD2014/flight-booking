import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOADS_FILE = os.path.join(BASE_DIR, 'assets/uploads')

class RestoAndHotels(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    imageFile = models.ImageField(upload_to=UPLOADS_FILE, default=os.path.join(BASE_DIR, 'assets/img/logo.png'))
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=7, default=1000)

    def __str__(self):
        return self.name

class Flights(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    dest = models.CharField(max_length=100, null=True)
    imageFile = models.ImageField(upload_to=UPLOADS_FILE, default=os.path.join(BASE_DIR, 'assets/img/logo.png'))
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=7, default=1000)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flights = models.ManyToManyField(Flights, blank=True)
    objects = models.ManyToManyField(RestoAndHotels, blank=True)

    def __str__(self):
        return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=User)

class PlannedFlights(models.Model):
    flights = models.OneToOneField(Flights, on_delete=models.SET_NULL, null=True)
    is_planned = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.flights.name
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Flights(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    desc = models.TextField()
    time_departure = models.DateTimeField(default=timezone.now, blank=True)
    time_arrival = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flights = models.ManyToManyField(Flights, blank=True)

    def __str__(self):
        return self.user.username

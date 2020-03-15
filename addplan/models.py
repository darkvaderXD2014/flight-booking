from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField(blank=True, null=True)
	address = models.CharField(max_length=100, null=True)
	price = models.DecimalField(blank=True, decimal_places=2, max_digits=7)

	def __str__(self):
		return self.name

class Hotels(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField(blank=True, null=True)
	address = models.CharField(max_length=100, null=True)
	price = models.DecimalField(blank=True, decimal_places=2, max_digits=7)

	def __str__(self):
		return self.name

class Flights(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField(blank=True, null=True)
	dest = models.CharField(max_length=100, null=True)
	price = models.DecimalField(blank=True, decimal_places=2, max_digits=7)

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	flights = models.ManyToManyField(Flights)
	hotels = models.ManyToManyField(Hotels)
	restaurant = models.ManyToManyField(Restaurant)

	def __str__(self):
		return self.user
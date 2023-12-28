from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class APIUser(AbstractUser):
    
    def get_username(self):
        return self.username
    
    def get_firstName(self):
        return self.first_name
    
    def get_lastName(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_full_name(self):
        return self.get_firstName() + " " + self.get_lastName()
    
    def __str__(self):
        return f'Username: {self.get_username()}\nFirst Name: {self.get_firstName()}\nLast Name: {self.get_lastName()}\nEmail: {self.get_email()}'

class Restaurant(models.Model):

    id = models.AutoField(primary_key=True)
    google_id = models.CharField(max_length=100, default='')
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100, default='')
    average_rating = models.FloatField()

    def get_id(self):
        return self.id
    
    def get_google_id(self):
        return self.google_id
    
    def get_longitude(self):
        return self.longitude
    
    def get_latitude(self):
        return self.latitude
    
    def get_location(self):
        return (self.get_longitude, self.get_latitude)
    
    def get_name(self):
        return self.name
    
    def get_average_rating(self):

        # Will have calculations in here in the future

        return self.average_rating

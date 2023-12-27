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
        return self.first_name() + " " + self.last_name()
    
    def __str__(self):
        return f'Username: {self.get_username()}\nFirst Name: {self.get_firstName()}\nLast Name: {self.get_lastName()}\nEmail: {self.get_email()}'

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
    
    def debug_string(self):
        return f'Username: {self.get_username()}\nFirst Name: {self.get_firstName()}\nLast Name: {self.get_lastName()}\nEmail: {self.get_email()}'
    
    def __str__(self):
        return self.get_username()

class Restaurant(models.Model):

    id = models.AutoField(primary_key=True)
    google_id = models.CharField(max_length=100, default='')
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100, default='')
    average_rating = models.FloatField()
    address = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, default='')
    price_level = models.CharField(max_length=100, default='')
    allows_dogs = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    dine_in = models.BooleanField(default=False)
    good_for_children = models.BooleanField(default=False)
    good_for_groups = models.BooleanField(default=False)
    outdoor_seating = models.BooleanField(default=False)

    def get_id(self):
        return self.id
    
    def get_google_id(self):
        return self.google_id
    
    def get_longitude(self):
        return self.longitude
    
    def get_latitude(self):
        return self.latitude
    
    def get_location(self):
        return (self.get_longitude(), self.get_latitude())
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address

    def get_type(self):
        return self.type

    def get_price_level(self):
        return self.price_level
    
    def get_allows_dogs(self):
        return self.allows_dogs
    
    def get_delivery(self):
        return self.delivery

    def get_dine_in(self):
        return self.dine_in
    
    def get_good_for_children(self):
        return self.good_for_children
    
    def get_good_for_groups(self):
        return self.good_for_groups
    
    def get_outdoor_seating(self):
        return self.outdoor_seating
    
    def get_categories(self):

        categories = RestaurantCategory.objects.filter(restaurant=self.get_id())

        list_of_categories = []

        for item in categories:

            category = Category.objects.get(category=item.get_category())
            list_of_categories.append(category)

        return list_of_categories
    
    def get_average_rating(self):

        # Will have calculations in here in the future

        return self.average_rating
    
    def debug_string(self):
        return f'ID: {self.get_id()}\nGoogle ID: {self.get_google_id()}\nLocation: {self.get_location()}\nName: {self.get_name()}\nAverage Rating: {self.get_average_rating()}'
    
    def __str__(self):
        return self.get_name()
    
class Review(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    description = models.TextField()

    def get_id(self):
        return self.id
    
    def get_user(self):
        return self.user
    
    def get_restaurant(self):
        return self.restaurant
    
    def get_rating(self):
        return self.rating
    
    def get_description(self):
        return self.description
    
    def debug_string(self):
        return f'ID: {self.get_id()}\nUser: {self.get_user()}\nRestaurant: {self.get_restaurant()}\nRating: {self.get_rating()}\nDescription: {self.get_description()}'
    
    def __str__(self):
        return f'{self.get_user()} -- {self.get_restaurant()}: {self.get_rating()}'
    
class Category(models.Model):

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100, default='')

    def get_id(self):
        return self.id
    
    def get_category(self):
        return self.category
    
    def debug_string(self):
        return f'ID: {self.get_id()}\nCategory: {self.get_category()}'

    def __str__(self):
        return f'{self.get_category()}'
    
class RestaurantCategory(models.Model):

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def get_id(self):
        return self.id
    
    def get_category(self):
        return self.category
    
    def get_restaurant(self):
        return self.restaurant
    
    def debug_string(self):
        return f'ID: {self.get_id()}\nCategory: {self.get_category()}\nRestaurant: {self.get_restaurant()}'
    
    def __str__(self):
        return f'{self.get_category()} -- {self.get_restaurant()}'
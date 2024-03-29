from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from .recommender import *
from django.utils import timezone

# Create your models here.
class APIUser(AbstractUser):
    
    # Getting the id of the class
    def get_id(self):
        return self.id

    # Getting the username of the class
    def get_username(self):
        return self.username
    
    # Getting the first name of the class
    def get_firstName(self):
        return self.first_name
    
    # Getting the last name of the class
    def get_lastName(self):
        return self.last_name
    
    # Getting the email
    def get_email(self):
        return self.email
    
    # Getting the full name of the class
    def get_full_name(self):
        return self.get_firstName() + " " + self.get_lastName()
    
    # Setting a new username for the instance
    def set_username(self, new_username):
        self.username = new_username
        return self.get_username()
    
    # Setting a new first name for the instance
    def set_firstName(self, new_first_name):
        self.first_name = new_first_name
        return self.get_firstName()
    
    # Setting a new last name for the instance
    def set_lastName(self, new_last_name):
        self.last_name = new_last_name
        return self.get_lastName()

    # Setting a new email name for the instance
    def set_email(self, new_email):
        self.email = new_email
        return self.get_email()

    # Getting the debug string of the class, set up so it includes important information when trying to debug using f strings
    def debug_string(self):
        return f'Username: {self.get_username()}\nFirst Name: {self.get_firstName()}\nLast Name: {self.get_lastName()}\nEmail: {self.get_email()}'
    
    # Converting to human readable format
    def __str__(self):
        return self.get_username()

# Class uses to save the hour and minute, that a restaurant could open/close
class RestaurantTime(models.Model):

    # Unique id for each instance of this class
    id = models.AutoField(primary_key=True)
    # Hour attribute, in the range between 0 and 23
    hour = models.IntegerField(choices=[(hour, hour) for hour in range(24)])
    # Minute attribute, in the range between 0 and 59
    minute = models.IntegerField(choices=[(minute, minute) for minute in range(60)])
    
    # Getting the id of the class
    def get_id(self):
        return self.id
    
    # Getting the hour of the class
    def get_hour(self):
        return self.hour
    
    # Getting the minute of the class
    def get_minute(self):
        return self.minute
    
    # Converting to human readable format
    def __str__(self):
        return f'{self.get_hour()}:{self.get_minute()}'

# Class uses to save the open time and close time of a restaurant for a given day
class RestaurantDay(models.Model):

    # Unique id for each instance of this class
    id = models.AutoField(primary_key=True)
    # open attribute, boolean to idenitfy if restaurant is open or closed on specific day
    open = models.BooleanField(default=True)
    # open_time attribute, instance of RestaurantTime of time at which restaurant opens
    open_time = models.ForeignKey(RestaurantTime, on_delete=models.CASCADE, related_name='open_time', blank=True, null=True)
    # close_time attribute, instance of RestaurantTime of time at which restaurant opens
    close_time = models.ForeignKey(RestaurantTime, on_delete=models.CASCADE, related_name='close_time', blank=True, null=True)

    # Getting the id of the class
    def get_id(self):
        return self.id
    
    # Getting the open attribute of the class
    def get_open(self):
        return self.open
    
    # Getting the open time of the class
    def get_open_time(self):
        return self.open_time
    
    # Getting the close time of the class
    def get_close_time(self):
        return self.close_time

    # Converting to human readable format  
    def __str__(self):
        # If the Restaurant does open return the timing in nice format and if it doesnt not open return "Closed"
        if self.get_open() == True:
            return f'{self.get_open_time()} - {self.get_close_time()}'
        return f'Closed'

# Class uses to save the open time and close time of a restaurant for each specific day of the week
class RestaurantHours(models.Model):

    # Unique id for each instance of this class
    id = models.AutoField(primary_key=True)
    # monday attribute, instance of RestaurantDay and saves the opening and closing time for that day
    monday = models.ForeignKey(RestaurantDay, on_delete=models.CASCADE, related_name='monday')
    # tuesday attribute, instance of RestaurantDay and saves the opening and closing time for that day
    tuesday = models.ForeignKey(RestaurantDay, on_delete=models.CASCADE, related_name='tuesday')
    # wednesday attribute, instance of RestaurantDay and saves the opening and closing time for that day
    wednesday = models.ForeignKey(RestaurantDay, on_delete=models.CASCADE, related_name='wednesday')
    # thursday attribute, instance of RestaurantDay and saves the opening and closing time for that day
    thursday = models.ForeignKey(RestaurantDay, on_delete=models.CASCADE, related_name='thursday')
    # friday attribute, instance of RestaurantDay and saves the opening and closing time for that day
    friday = models.ForeignKey(RestaurantDay, on_delete=models.CASCADE, related_name='friday')
    # saturday attribute, instance of RestaurantDay and saves the opening and closing time for that day
    saturday = models.ForeignKey(RestaurantDay, on_delete=models.CASCADE, related_name='saturday')
    # sunday attribute, instance of RestaurantDay and saves the opening and closing time for that day
    sunday = models.ForeignKey(RestaurantDay, on_delete=models.CASCADE, related_name='sunday')

    # Getting the id of the class
    def get_id(self):
        return self.id
    
    # Getting the attribute monday for the class
    def get_monday(self):
        return self.monday
    
    # Getting the attribute tuesday for the class
    def get_tuesday(self):
        return self.tuesday
    
    # Getting the attribute wednesday for the class
    def get_wednesday(self):
        return self.wednesday
    
    # Getting the attribute thursday for the class
    def get_thursday(self):
        return self.thursday
    
    # Getting the attribute friday for the class
    def get_friday(self):
        return self.friday
    
    # Getting the attribute saturday for the class
    def get_saturday(self):
        return self.saturday
    
    # Getting the attribute sunday for the class
    def get_sunday(self):
        return self.sunday
    
    # Converting to human readable format
    def __str__(self):
        return f'Monday: {self.get_monday()}\nTuesday: {self.get_tuesday()}\nWednesday: {self.get_wednesday()}\nThursday: {self.get_thursday()}\nFriday: {self.get_friday()}\nSaturday: {self.get_saturday()}\nSunday: {self.get_sunday()}'

# Class uses to save information about each restaurant
class Restaurant(models.Model):

    # Choices for restaurant price levels
    restaurant_price_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    # Unique id for each instance of this class
    id = models.AutoField(primary_key=True)
    # unique id used by google for each instance of this class
    google_id = models.CharField(max_length=100, default='')
    # longitude co-ordinate attribute
    longitude = models.FloatField()
    # latitude co-ordinate attribute
    latitude = models.FloatField()
    # name attribute for the class
    name = models.CharField(max_length=100, default='')
    # average rating of reviews for this restaurant
    average_rating = models.FloatField()
    # address of this restaurant
    address = models.CharField(max_length=100, default='')
    # main type of the restaurant
    type = models.CharField(max_length=100, default='')
    # price level of the restaurant
    price_level = models.CharField(max_length=100, choices=restaurant_price_choices, default='low')
    # allow dogs attribute which is boolean
    allows_dogs = models.BooleanField(default=False)
    # delivery attribute which is boolean
    delivery = models.BooleanField(default=False)
    # dine in attribute which is boolean
    dine_in = models.BooleanField(default=False)
    # good for children dogs attribute which is boolean
    good_for_children = models.BooleanField(default=False)
    # good for groups dogs attribute which is boolean
    good_for_groups = models.BooleanField(default=False)
    # outdoor seating dogs attribute which is boolean
    outdoor_seating = models.BooleanField(default=False)
    # hours attribute, instance of the RestaurantHours class
    hours = models.ForeignKey(RestaurantHours, on_delete=models.CASCADE, blank=True, null=True)
    # number of reviews
    review_number = models.IntegerField(default=0)

    # Getting the id of the class
    def get_id(self):
        return self.id
    
    # Getting the google id of the class
    def get_google_id(self):
        return self.google_id
    
    # Getting the longitude of the class
    def get_longitude(self):
        return self.longitude
    
    # Getting the latitude of the class
    def get_latitude(self):
        return self.latitude
    
    # Getting the location, (longitude, latitude), of the class
    def get_location(self):
        return (self.get_longitude(), self.get_latitude())
    
    # Getting the name of the class
    def get_name(self):
        return self.name
    
    # Getting the address of the class
    def get_address(self):
        return self.address

    # Getting the type of the class
    def get_type(self):
        return self.type

    # Getting the price_level of the class
    def get_price_level(self):
        return self.price_level
    
    # Getting the allow dogs boolean of the class
    def get_allows_dogs(self):
        return self.allows_dogs
    
    # Getting the delivery boolean of the class
    def get_delivery(self):
        return self.delivery

    # Getting the dine in boolean of the class
    def get_dine_in(self):
        return self.dine_in
    
    # Getting the good for children boolean of the class
    def get_good_for_children(self):
        return self.good_for_children
    
    # Getting the good for groups boolean of the class
    def get_good_for_groups(self):
        return self.good_for_groups
    
    # Getting the outdoor seating boolean of the class
    def get_outdoor_seating(self):
        return self.outdoor_seating
    
    # Getting the RestaurantHours instance for the class
    def get_hours(self):
        return self.hours
    
    # Getting all the categories associated with the class
    def get_categories(self):

        # Getting all RestaurantCategory instances with restaurant_id of the current restaurant
        categories = RestaurantCategory.objects.filter(restaurant=self.get_id())

        list_of_categories = []

        # Looping through each instance saving the category
        for item in categories:

            # Getting the specific instance of the category and appending to list
            category = Category.objects.get(category=item.get_category())
            list_of_categories.append(category)

        # Returning the list of categorys
        return list_of_categories
    
    # Getting the average rating of the restaurant instance
    def get_average_rating(self):

        # Getting all Review instances with restaurant_id of the current restaurant
        queryset = Review.objects.filter(restaurant_id=self.get_id())

        # Divisor will be the total number of reviews returned
        divisor = len(queryset)
        total = 0

        # If no reviews returned then just return 0 as there is reviews created
        if divisor == 0:
            return 0
        
        current_reviews = self.get_review_number()

        # if the number of reviews is the same as there was last run then dont calculate
        if current_reviews == divisor:
            return self.average_rating
        
        # if the number of reviews is different then save the new value
        self.review_number = divisor

        # Loop through the reviews adding up all the ratings 
        for item in queryset:
            total += item.get_rating()
        
        # Set the average rating to the result
        self.average_rating = round(total / divisor, 1)

        # Save the average rating
        self.save()

        # Return the result
        return self.average_rating
    
    # Getting the review number value for the class
    def get_review_number(self):
        return self.review_number
    
    # Getting the debug string of the class, set up so it includes important information when trying to debug using f strings
    def debug_string(self):
        return f'ID: {self.get_id()}\nGoogle ID: {self.get_google_id()}\nLocation: {self.get_location()}\nName: {self.get_name()}\nAverage Rating: {self.get_average_rating()}'
    
    # Converting to human readable format
    def __str__(self):
        return self.get_name()

# Class uses to save information about each review created
class Review(models.Model):

    # Unique id for each instance of this class
    id = models.AutoField(primary_key=True)
    # user attribute, instance of the APIUser class
    user = models.ForeignKey(APIUser, on_delete=models.CASCADE)
    # restaurant attribute, instance of the Restaurant class
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # rating attribute, can be either 1,2,3,4,5
    rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    # description attribute, textfield
    description = models.TextField()
    # created at time, datetimefield
    date = models.DateField(default=timezone.now)
    # positive or negative value
    sentiment = models.IntegerField(choices=[(1,1),(2,2)], default=0)

    # Getting the id of the class
    def get_id(self):
        return self.id
    
    # Getting the user of the class
    def get_user(self):
        return self.user
    
    # Getting the restaurant of the class
    def get_restaurant(self):
        return self.restaurant
    
    # Getting the rating of the class
    def get_rating(self):
        return self.rating
    
    # Getting the description of the class
    def get_description(self):
        return self.description
    
    def get_date(self):
        return self.date
    
    def get_sentiment(self):
        return self.sentiment
    
    # Getting the debug string of the class, set up so it includes important information when trying to debug using f strings
    def debug_string(self):
        return f'ID: {self.get_id()}\nUser: {self.get_user()}\nRestaurant: {self.get_restaurant()}\nRating: {self.get_rating()}\nDescription: {self.get_description()}'
    
    # Converting to human readable format
    def __str__(self):
        return f'{self.get_user()} -- {self.get_restaurant()}: {self.get_rating()}'
    
# Class uses to save information about each unqiue category
class Category(models.Model):

    # Unique id for each instance of this class
    id = models.AutoField(primary_key=True)
    # category attribute, unique category name for each instance
    category = models.CharField(max_length=100, default='')

    # Getting the id of the class
    def get_id(self):
        return self.id
    
    # Getting the category of the class
    def get_category(self):
        return self.category

    # Getting the debug string of the class, set up so it includes important information when trying to debug using f strings
    def debug_string(self):
        return f'ID: {self.get_id()}\nCategory: {self.get_category()}'

    # Converting to human readable format
    def __str__(self):
        return f'{self.get_category()}'
    
# Class used to link a instance of category to the instance of restaurant
class RestaurantCategory(models.Model):

    # Unique id for each instance of this class
    id = models.AutoField(primary_key=True)
    # category attribute, instance of the category class
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # restaurant attribute, instance of the restaurant class
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    # Getting the id of the class
    def get_id(self):
        return self.id
    
    # Getting the category of the class
    def get_category(self):
        return self.category
    
    # Getting the restaurant of the class
    def get_restaurant(self):
        return self.restaurant
    
    # Getting the debug string of the class, set up so it includes important information when trying to debug using f strings
    def debug_string(self):
        return f'ID: {self.get_id()}\nCategory: {self.get_category()}\nRestaurant: {self.get_restaurant()}'
    
    # Converting to human readable format
    def __str__(self):
        return f'{self.get_category()} -- {self.get_restaurant()}'
    

""" 
Stack Overflow. (2018, April 9). Answer by Ramkishore M on "How to implement Singleton in Django" [Answer]. from https://stackoverflow.com/a/49736970

Code used to design the singleton class model.
"""

class SingletonModel(models.Model): # Singleton class so only 1 instance can be created
    class Meta:
        abstract = True

    def save(self, *args, **kwargs): # Saves the method with pk 1
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1) # Gets the instance with pk 1
        return obj

# HybirdRecommender inherits from SingletonModel, saves all recommender models
class HybridRecommender(SingletonModel):

    # Collaborative model attribute, saved as a binary field
    collaborative_model = models.BinaryField()
    # content model attribute, saved as a binary field
    content_model = models.BinaryField()
    # restaurant id masking attribute, saved as a text field
    restaurant_id_masking = models.TextField()

    # Starts both recommendation systems on backend startup
    def start_recommender(self):

        # Saves the collaborative filtering model to instance
        self.collaborative_model = start_collaborative_recommender()
        # Saves the content filtering model to instance and the restaurant_id masking
        self.content_model, self.restaurant_id_masking = start_content_recommender()
        # Save singleton model
        self.save()

    # Updates collaborative recommender when new information is added
    def update_collaborative_recommender(self):

        # Saves the collaborative filtering model to instance
        self.collaborative_model = start_collaborative_recommender()
        # Save singleton model
        self.save()

    # Updates content recommender when new information is added
    def update_content_recommender(self):

        # Saves the content filtering model to instance and the restaurant_id masking
        self.content_model, self.restaurant_id_masking = start_content_recommender()
        # Save singleton model
        self.save()

    # Query the content recommender, inputting a restaurant_id and outputting a list of similar restaurants
    def query_content_recommender(self, restaurant_id):

        # calls function to get similar restaurants, passing in content model, restaurant id to query and the restaurant id masking
        similar_restaurants = get_content_recommendations(self.content_model, restaurant_id, self.restaurant_id_masking)

        # return list of similar restaurants
        return similar_restaurants
    
    # Query the collaborative recommender, inputting a user_id and outputting a list of similar restaurants
    def query_collaborative_recommender(self, user_id):

        # calls function to get similar restaurants, passing in collabl model and user id
        recommended_restaurants = get_collaborative_recommendations(self.collaborative_model, user_id)

        # return list of similar restaurants
        return recommended_restaurants
    
    # Query the hybrid recommender, inputting a user_id and outputting a list of similar restaurants
    def query_hybrid_recommender(self, user_id):

        # First query the collab recommender, using the user_id and get a list of restaurants
        collab_recommended_restaurants = get_collaborative_recommendations(self.collaborative_model, user_id)

        hybrid_recommendations = []

        # Loop through the list of recommendations and input to content recommender to further generate recommendations
        for id in collab_recommended_restaurants:

            hybrid_recommendations.append(id)
            hybrid_recommendations.extend(get_content_recommendations(self.content_model, id, self.restaurant_id_masking))

        # Return the hybrid recommendations list
        return hybrid_recommendations
    
    # Query the collaborative recommender to get recommendations using a restaurant list
    def query_list_collaborative_recommender(self, user_id, restaurant_id_list):

        # Get the results of which are highest 10% predicted ratings
        results = get_collaborative_recommender_from_list(self.collaborative_model, user_id, restaurant_id_list)

        return results
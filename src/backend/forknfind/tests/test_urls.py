from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from ..views import *
from ..models import *
import random

# Unit tests for the APIRegisterUser API
class APIRegisterUserTests(APITestCase):

    # Needed as after a user's account is created the recommender updates for that new user
    # Initial set up of data
    # Creates 1 instance of the class HybridRecommender 
    # Creates 20 instances of the class APIUser
    # Creates 20 instances of the class Restaurant
    # Creates 100 instances of the class Review
    # Creates 1 isntance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
    # Creates 2 instances of the class Category
    # Creates 2 instances of the class RestaurantCategory
    def setUpTestData():

        HybridRecommender.objects.create()

        # Create 20 unique users
        for i in range(1, 21):
            APIUser.objects.create(
            username='dalye54' + str(i),
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

        RestaurantDay.objects.create(
            open=False
        )

        restaurant_day = RestaurantDay.objects.get(id=1)

        RestaurantHours.objects.create(
            monday=restaurant_day,
            tuesday=restaurant_day,
            wednesday=restaurant_day,
            thursday=restaurant_day,
            friday=restaurant_day,
            saturday=restaurant_day,
            sunday=restaurant_day,
        )

        restaurant_hours = RestaurantHours.objects.get(id=1)

        # Create 10 unique restaurants with these attributes and link them to the categories with id 1 and 2
        for i in range(1,11):
            Restaurant.objects.create(
                google_id='google_id_583589498278432',
                longitude=43.78,
                latitude=17.35,
                name='A Pizza Place',
                address='Dublin',
                type='pizza',
                price_level='PRICE_LEVEL_INEXPENSIVE',
                allows_dogs=True,
                delivery=False,
                dine_in=True,
                good_for_children=True,
                good_for_groups=False,
                outdoor_seating=False,
                average_rating=0,
                hours=restaurant_hours
            )

        # Create 10 more unique restaurants with these attributes and link them to the categories with id 3 and 4
        for i in range(1,11):
            Restaurant.objects.create(
                google_id='google_id_392483294832478', 
                longitude=70.14,
                latitude=23.95,
                name='A Pasta Place',
                address='New York',
                type='Pasta',
                price_level='PRICE_LEVEL_EXPENSIVE',
                allows_dogs=False,
                delivery=True,
                dine_in=False,
                good_for_children=False,
                good_for_groups=True,
                outdoor_seating=True,
                average_rating=0,
                hours=restaurant_hours
            )

            restaurant = Restaurant.objects.get(id=i + 10) 

        # Create 100 unique reviews in total, with each user having 5 reviews for a random 5 restaurants
        for i in range(1, 21):
            user = APIUser.objects.get(id=i)
            for _ in range(5):
                Review.objects.create(
                    user=user,
                    restaurant=Restaurant.objects.get(id=random.randint(1,20)),
                    rating=(random.randint(1,5)),
                    description="Restaurant"
                )

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):

        self.client = APIClient()


    def test_post_api_register_user(self):

        # data to create new user
        data = {"username": "johndoe", "password": "password", "email": "test@gmail.com", "first_name": "john", "last_name": "doe"}

        # post the data to the url in json format
        response = self.client.post("/register/user/", data=data, format="json")

        # verify the response data has been created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get the created user
        user = APIUser.objects.get(id=21)

        # verify the data in the user is the same as what we sent
        self.assertEqual(user.get_username(), data['username'])
        self.assertEqual(user.get_email(),data['email'])
        self.assertEqual(user.get_firstName(),data['first_name'])
        self.assertEqual(user.get_lastName(),data['last_name'])
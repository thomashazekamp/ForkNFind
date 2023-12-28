from django.test import TestCase
from .models import *

# Create your tests here.
class APIUserMethodTests(TestCase):

    # Set up an instance of the APIUser class
    def setUp(self):

        self.model_instance = APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

    def test_get_username(self):

        username = self.model_instance.get_username()
        correct_username = "dalye54"
        self.assertEqual(username, correct_username)
    
    def test_get_firstName(self):

        first_name = self.model_instance.get_firstName()
        correct_first_name = "Eoin"
        self.assertEqual(first_name, correct_first_name)

    def test_get_lastName(self):

        last_name = self.model_instance.get_lastName()
        correct_last_name = "Daly"
        self.assertEqual(last_name, correct_last_name)

    def test_get_email(self):

        email = self.model_instance.get_email()
        correct_email = "eoin.daly54@mail.dcu.ie"
        self.assertEqual(email, correct_email)

    def test_get_full_name(self):

        full_name = self.model_instance.get_full_name()
        correct_full_name = "Eoin Daly"
        self.assertEqual(full_name, correct_full_name)

    def test_print_user_details(self):
        
        print_format = str(self.model_instance)
        correct_print_format = f'Username: dalye54\nFirst Name: Eoin\nLast Name: Daly\nEmail: eoin.daly54@mail.dcu.ie'
        self.assertEqual(print_format, correct_print_format)

class APIRestaurantMethodTests(TestCase):

    def setUp(self):

        self.model_instance = Restaurant.objects.create(
            google_id='google_id_583589498278432',
            longitude=43.78,
            latitude=17.35,
            name='A Pizza Place',
            average_rating=0,
        )

    def test_get_id(self):

        id = self.model_instance.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    def test_get_google_id(self):

        google_id = self.model_instance.get_google_id()
        correct_google_id = "google_id_583589498278432"
        self.assertEqual(google_id, correct_google_id)

    def test_get_longitude(self):

        longitude = self.model_instance.get_longitude()
        correct_longitude = 43.78
        self.assertEqual(longitude, correct_longitude)

    # To test the it is not rounding the number
    def test_get_longitude_fail_case(self):

        longitude = self.model_instance.get_longitude()
        correct_longitude = 44
        self.assertNotEqual(longitude, correct_longitude)

    def test_get_latitude(self):

        latitude = self.model_instance.get_latitude()
        correct_latitude = 17.35
        self.assertEqual(latitude, correct_latitude)

    # To test the it is not rounding the number
    def test_get_latitude_fail_case(self):

        latitude = self.model_instance.get_latitude()
        correct_latitude = 17
        self.assertNotEqual(latitude, correct_latitude)

    def test_get_location(self):

        location = self.model_instance.get_location()
        correct_location = (43.78, 17.35)
        self.assertEqual(location, correct_location)

    def test_get_name(self):
        name = self.model_instance.get_name()
        correct_name = "A Pizza Place"
        self.assertEqual(name, correct_name)

    def test_get_average_rating(self):
        average_rating = self.model_instance.get_average_rating()
        correct_average_rating = 0
        self.assertEqual(average_rating, correct_average_rating)

    def test_print_user_details(self):
        print_format = str(self.model_instance)
        correct_print_format = f'ID: 1\nGoogle ID: google_id_583589498278432\nLocation: (43.78, 17.35)\nName: A Pizza Place\nAverage Rating: 0'
        self.assertEqual(print_format, correct_print_format)

class APIReviewMethodTests(TestCase):

    def setUp(self):

        self.user = APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

        self.restaurant = Restaurant.objects.create(
            google_id='google_id_583589498278432',
            longitude=43.78,
            latitude=17.35,
            name='A Pizza Place',
            average_rating=0,
        )
      
        self.model_instance = Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            rating=1,
            description='I had a great time :).'
        )

    def test_get_id(self):

        id = self.model_instance.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    def test_get_user(self):
        user = self.model_instance.get_user()
        correct_user = self.user
        self.assertEqual(user, correct_user)

    def test_get_restaurant(self):

        restaurant = self.model_instance.get_restaurant()
        correct_restaurant = self.restaurant
        self.assertEqual(restaurant, correct_restaurant)

    def test_get_rating(self):

        rating = self.model_instance.get_rating()
        correct_rating = 1
        self.assertEqual(rating, correct_rating)

    def test_get_description(self):

        description = self.model_instance.get_description()
        correct_description = "I had a great time :)."
        self.assertEqual(description, correct_description)
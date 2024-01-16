from django.test import TestCase
from .models import *
from .formula import *

# Unit tests for the APIUser class
class APIUserMethodTests(TestCase):

    # Initial set up of data
    # Creates 1 instance of the class APIUser
    def setUpTestData():

        APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

    # Test to validate the get_id() method
    # Expected result is that the id 1 is returned from the method
    def test_get_id(self):

        user = APIUser.objects.get(id=1)
        id = user.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    # Test to validate the get_username() method
    # Expected result is that the username 'dalye54' is returned from the method
    def test_get_username(self):

        user = APIUser.objects.get(id=1)
        username = user.get_username()
        correct_username = "dalye54"
        self.assertEqual(username, correct_username)
    
    # Test to validate the get_firstName() method
    # Expected result is that the firstName 'Eoin' is returned from the method
    def test_get_firstName(self):

        user = APIUser.objects.get(id=1)
        first_name = user.get_firstName()
        correct_first_name = "Eoin"
        self.assertEqual(first_name, correct_first_name)

    # Test to validate the get_lastName() method
    # Expected result is that the lastName 'Daly' is returned from the method
    def test_get_lastName(self):

        user = APIUser.objects.get(id=1)
        last_name = user.get_lastName()
        correct_last_name = "Daly"
        self.assertEqual(last_name, correct_last_name)

    # Test to validate the get_email() method
    # Expected result is that the email 'eoin.daly54@mail.dcu.ie' is returned from the method
    def test_get_email(self):

        user = APIUser.objects.get(id=1)
        email = user.get_email()
        correct_email = "eoin.daly54@mail.dcu.ie"
        self.assertEqual(email, correct_email)

    # Test to validate the get_full_name() method
    # Expected result is that the full_name 'Eoin Daly' is returned from the method
    def test_get_full_name(self):

        user = APIUser.objects.get(id=1)
        full_name = user.get_full_name()
        correct_full_name = "Eoin Daly"
        self.assertEqual(full_name, correct_full_name)

    # Test to validate the set_username() method
    # Expected result is that the username for the instance is changed to "testuser1"
    def test_set_username(self):

        user = APIUser.objects.get(id=1)
        username = user.set_username("testuser1")
        correct_username = "testuser1"
        self.assertEqual(username, correct_username)

    # Test to validate the set_firstName() method
    # Expected result is that the first_name for the instance is changed to "Ronaldo"
    def test_set_firstName(self):

        user = APIUser.objects.get(id=1)
        first_name = user.set_firstName("Ronaldo")
        correct_first_name = "Ronaldo"
        self.assertEqual(first_name, correct_first_name)

    # Test to validate the set_lastName() method
    # Expected result is that the last_name for the instance is changed to "Ronaldo"
    def test_set_lastName(self):

        user = APIUser.objects.get(id=1)
        last_name = user.set_lastName("Ronaldo")
        correct_last_name = "Ronaldo"
        self.assertEqual(last_name, correct_last_name)

    # Test to validate the set_email() method
    # Expected result is that the email for the instance is changed to "test@gmail.com"
    def test_set_email(self):

        user = APIUser.objects.get(id=1)
        email = user.set_email("test@gmail.com")
        correct_email = "test@gmail.com"
        self.assertEqual(email, correct_email)

    # Test to validate the get_debug_string() method
    # Expected result is that the full_name f'Username: dalye54\nFirst Name: Eoin\nLast Name: Daly\nEmail: eoin.daly54@mail.dcu.ie' is returned from the method
    def test_debug_string(self):
        
        user = APIUser.objects.get(id=1)
        debug_format = user.debug_string()
        correct_debug_format = f'Username: dalye54\nFirst Name: Eoin\nLast Name: Daly\nEmail: eoin.daly54@mail.dcu.ie'
        self.assertEqual(debug_format, correct_debug_format)

    # Test to validate the __str__() method
    # Expected result is that 'dalye54' is returned from the method
    def test_to_string(self):

        user = APIUser.objects.get(id=1)
        to_string = str(user)
        correct_to_string = "dalye54"
        self.assertEqual(to_string, correct_to_string)

class APIRestaurantMethodTests(TestCase):

    def setUp(self):

        self.restaurant_day = RestaurantDay.objects.create(
            open=False
        )

        self.restaurant_hours = RestaurantHours.objects.create(
            monday=self.restaurant_day,
            tuesday=self.restaurant_day,
            wednesday=self.restaurant_day,
            thursday=self.restaurant_day,
            friday=self.restaurant_day,
            saturday=self.restaurant_day,
            sunday=self.restaurant_day
        )

        self.model_instance = Restaurant.objects.create(
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
            hours=self.restaurant_hours
        )

        self.category = Category.objects.create(
            category='Chinese'
        )

        self.restaurant_category = RestaurantCategory.objects.create(
            category=self.category,
            restaurant=self.model_instance
        )

        self.category_2 = Category.objects.create(
            category='Indian'
        )

        self.restaurant_category_2 = RestaurantCategory.objects.create(
            category=self.category_2,
            restaurant=self.model_instance
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

    def test_get_address(self):
        address = self.model_instance.get_address()
        correct_address = 'Dublin'
        self.assertEqual(address, correct_address)

    def test_get_type(self):
        type = self.model_instance.get_type()
        correct_type = 'pizza'
        self.assertEqual(type, correct_type)

    def test_get_price_level(self):
        price_level = self.model_instance.get_price_level()
        correct_price_level = 'PRICE_LEVEL_INEXPENSIVE'
        self.assertEqual(price_level, correct_price_level)

    def test_get_allows_dogs(self):
        allows_dogs = self.model_instance.get_allows_dogs()
        correct_allows_dogs = True
        self.assertEqual(allows_dogs, correct_allows_dogs)

    def test_get_delivery(self):
        delivery = self.model_instance.get_delivery()
        correct_delivery = False
        self.assertEqual(delivery, correct_delivery)

    def test_get_dine_in(self):
        dine_in = self.model_instance.get_dine_in()
        correct_dine_in = True
        self.assertEqual(dine_in, correct_dine_in)

    def test_get_good_for_children(self):
        good_for_children = self.model_instance.get_good_for_children()
        correct_good_for_children = True
        self.assertEqual(good_for_children, correct_good_for_children)

    def test_get_good_for_groups(self):
        good_for_groups = self.model_instance.get_good_for_groups()
        correct_good_for_groups = False
        self.assertEqual(good_for_groups, correct_good_for_groups)

    def test_get_outdoor_seating(self):
        outdoor_seating = self.model_instance.get_outdoor_seating()
        correct_outdoor_seating = False
        self.assertEqual(outdoor_seating, correct_outdoor_seating)

    def test_get_hours(self):
        hours = self.model_instance.get_hours()
        correct_hours = self.restaurant_hours
        self.assertEqual(hours, correct_hours)

    def test_get_categories(self):

        categories = self.model_instance.get_categories()
        category_names = [category.get_category() for category in categories]
        correct_categories = ["Chinese", "Indian"]
        self.assertEqual(category_names, correct_categories)

    def test_get_average_rating(self):

        average_rating = self.model_instance.get_average_rating()
        correct_average_rating = 0
        self.assertEqual(average_rating, correct_average_rating)

    def test_debug_string(self):

        debug_format = self.model_instance.debug_string()
        correct_debug_format = f'ID: 1\nGoogle ID: google_id_583589498278432\nLocation: (43.78, 17.35)\nName: A Pizza Place\nAverage Rating: 0'
        self.assertEqual(debug_format, correct_debug_format)

    def test_to_string(self):

        to_string = str(self.model_instance)
        correct_to_string = "A Pizza Place"
        self.assertEqual(to_string, correct_to_string)

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

    def test_debug_string(self):

        debug_format = self.model_instance.debug_string()
        correct_debug_format = f'ID: 1\nUser: dalye54\nRestaurant: A Pizza Place\nRating: 1\nDescription: I had a great time :).'
        self.assertEqual(debug_format, correct_debug_format)

    def test_to_string(self):

        to_string = str(self.model_instance)
        correct_to_string = "dalye54 -- A Pizza Place: 1"
        self.assertEqual(to_string, correct_to_string)

class CategoryMethodTests(TestCase):

    def setUp(self):

        self.model_instance = Category.objects.create(
            category="Chinese"
        )

    def test_get_id(self):

        id = self.model_instance.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    def test_get_category(self):

        category = self.model_instance.get_category()
        correct_category = "Chinese"
        self.assertEqual(category, correct_category)

    def test_debug_string(self):

        debug_format = self.model_instance.debug_string()
        correct_debug_format = f'ID: 1\nCategory: Chinese'
        self.assertEqual(debug_format, correct_debug_format)

    def test_to_string(self):

        to_string = str(self.model_instance)
        correct_to_string = "Chinese"
        self.assertEqual(to_string, correct_to_string)

class RestaurantCategoryTests(TestCase):

    def setUp(self):

        self.restaurant = Restaurant.objects.create(
            google_id='google_id_583589498278432',
            longitude=43.78,
            latitude=17.35,
            name='A Pizza Place',
            average_rating=0,
        )

        self.category = Category.objects.create(
            category='Chinese'
        )

        self.model_instance = RestaurantCategory.objects.create(

            category=self.category,
            restaurant=self.restaurant,
        )

    def test_get_id(self):

        id = self.model_instance.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    def test_get_category(self):

        category = self.model_instance.get_category()
        correct_category = self.category
        self.assertEqual(category, correct_category)

    def test_get_restaurant(self):

        restaurant = self.model_instance.get_restaurant()
        correct_restaurant = self.restaurant
        self.assertEqual(restaurant, correct_restaurant)

    def test_debug_string(self):

        debug_format = self.model_instance.debug_string()
        correct_debug_format = f'ID: 1\nCategory: Chinese\nRestaurant: A Pizza Place'
        self.assertEqual(debug_format, correct_debug_format)

    def test_to_string(self):

        to_string = str(self.model_instance)
        correct_to_string = "Chinese -- A Pizza Place"
        self.assertEqual(to_string, correct_to_string)

class APIRestaurantTimeMethodTests(TestCase):

    def setUp(self):

        self.model_instance = RestaurantTime.objects.create(
            hour=12,
            minute=30
        )

    def test_get_id(self):

        id = self.model_instance.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    def test_get_hour(self):

        hour = self.model_instance.get_hour()
        correct_hour = 12
        self.assertEqual(hour, correct_hour)

    def test_get_minute(self):

        minute = self.model_instance.get_minute()
        correct_minute = 30
        self.assertEqual(minute, correct_minute)

    def test_to_string(self):

        to_string = str(self.model_instance)
        correct_to_string = '12:30'
        self.assertEqual(to_string, correct_to_string)

class APIRestaurantDayMethodTests(TestCase):

    def setUp(self):

        self.restaurant_time_open = RestaurantTime.objects.create(
            hour=12,
            minute=30
        )

        self.restaurant_time_close = RestaurantTime.objects.create(
            hour=18,
            minute=45
        )

        self.model_instance = RestaurantDay.objects.create(
            open=True,
            open_time=self.restaurant_time_open,
            close_time=self.restaurant_time_close
        )

        self.model_instance_not_open = RestaurantDay.objects.create(
            open=False
        )

    def test_get_id(self):

        id = self.model_instance.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

        id = self.model_instance_not_open.get_id()
        correct_id = 2
        self.assertEqual(id, correct_id)

    def test_get_open(self):

        open = self.model_instance.get_open()
        correct_open = True
        self.assertEqual(open, correct_open)

        open = self.model_instance_not_open.get_open()
        correct_open = False
        self.assertEqual(open, correct_open)

    def test_get_open_time(self):

        open_time = self.model_instance.get_open_time()
        correct_open_time = self.restaurant_time_open
        self.assertEqual(open_time, correct_open_time)

        open_time = self.model_instance_not_open.get_open_time()
        correct_open_time = None
        self.assertEqual(open_time, correct_open_time)

    def test_get_close_time(self):

        close_time = self.model_instance.get_close_time()
        correct_close_time = self.restaurant_time_close
        self.assertEqual(close_time, correct_close_time)

        close_time = self.model_instance_not_open.get_open_time()
        correct_close_time = None
        self.assertEqual(close_time, correct_close_time)

    def test_to_string(self):

        to_string = str(self.model_instance)
        correct_to_string = '12:30 - 18:45'
        self.assertEqual(to_string, correct_to_string)

        to_string = str(self.model_instance_not_open)
        correct_to_string = 'Closed'
        self.assertEqual(to_string, correct_to_string)

class APIRestaurantHoursMethodTests(TestCase):

    def setUp(self):

        self.restaurant_time_open = RestaurantTime.objects.create(
            hour=12,
            minute=30
        )

        self.restaurant_time_close = RestaurantTime.objects.create(
            hour=18,
            minute=45
        )

        self.restaurant_day_1 = RestaurantDay.objects.create(
            open=True,
            open_time=self.restaurant_time_open,
            close_time=self.restaurant_time_close
        )

        self.restaurant_day_2 = RestaurantDay.objects.create(
            open=False
        )

        self.model_instance = RestaurantHours.objects.create(
            monday=self.restaurant_day_2,
            tuesday=self.restaurant_day_1,
            wednesday=self.restaurant_day_1,
            thursday=self.restaurant_day_1,
            friday=self.restaurant_day_1,
            saturday=self.restaurant_day_2,
            sunday=self.restaurant_day_2
        )

    def test_get_id(self):

        id = self.model_instance.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    def test_get_monday(self):

        monday = self.model_instance.get_monday()
        correct_monday = self.restaurant_day_2
        self.assertEqual(monday, correct_monday)

    def test_get_tuesday(self):

        tuesday = self.model_instance.get_tuesday()
        correct_tuesday = self.restaurant_day_1
        self.assertEqual(tuesday, correct_tuesday)

    def test_get_wednesday(self):

        wednesday = self.model_instance.get_wednesday()
        correct_wednesday = self.restaurant_day_1
        self.assertEqual(wednesday, correct_wednesday)

    def test_get_thursday(self):

        thursday = self.model_instance.get_thursday()
        correct_thursday = self.restaurant_day_1
        self.assertEqual(thursday, correct_thursday)

    def test_get_friday(self):

        friday = self.model_instance.get_friday()
        correct_friday = self.restaurant_day_1
        self.assertEqual(friday, correct_friday)

    def test_get_saturday(self):

        saturday = self.model_instance.get_saturday()
        correct_saturday = self.restaurant_day_2
        self.assertEqual(saturday, correct_saturday)

    def test_get_sunday(self):

        sunday = self.model_instance.get_sunday()
        correct_sunday = self.restaurant_day_2
        self.assertEqual(sunday, correct_sunday)

    def test_to_string(self):

        to_string = str(self.model_instance)
        correct_to_string = f'Monday: Closed\nTuesday: 12:30 - 18:45\nWednesday: 12:30 - 18:45\nThursday: 12:30 - 18:45\nFriday: 12:30 - 18:45\nSaturday: Closed\nSunday: Closed'
        self.assertEqual(to_string, correct_to_string)

class haversineFormulaTests(TestCase):

    # Equal to 0
    def test_get_distance(self):

        place_1 = (10,20)
        place_2 = (10,20)

        correct_distance = 0
        distance = haversine(place_1, place_2)

        self.assertEqual(correct_distance, distance)

    # Equal to non zero number 0
    def test_get_distance(self):

        place_1 = (5,10)
        place_2 = (10,20)

        correct_distance = 1234.4754736585755
        distance = haversine(place_1, place_2)

        self.assertEqual(correct_distance, distance)
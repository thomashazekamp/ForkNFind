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

# Unit tests for the Restaurant class
class RestaurantMethodTests(TestCase):

    # Initial set up of data
    # Creates 1 instance of the class Restaurant
    # Creates 1 instance of the class RestaurantHours
    # Creates 1 instance of the class RestaurantDay
    # Creates 2 instances of the class Category
    # Creates 2 instances of the class RestaurantCategory
    # Creates 2 instances of the class Review
    def setUpTestData():

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

        restaurant = Restaurant.objects.get(id=1)

        Category.objects.create(
            category='Chinese'
        )

        category = Category.objects.get(id=1)

        RestaurantCategory.objects.create(
            category=category,
            restaurant=restaurant
        )

        Category.objects.create(
            category='Indian'
        )

        category_2 = Category.objects.get(id=2)

        RestaurantCategory.objects.create(
            category=category_2,
            restaurant=restaurant
        )

        APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

        user = APIUser.objects.get(id=1)

        Review.objects.create(
            user=user,
            restaurant=restaurant,
            rating=4,
            description="Lovely Restaurant"
        )

        Review.objects.create(
            user=user,
            restaurant=restaurant,
            rating=2,
            description="Terrible Restaurant"
        )

    # Test to validate the get_id() method
    # Expected result is that the id 1 is returned from the method
    def test_get_id(self):

        restaurant = Restaurant.objects.get(id=1)
        id = restaurant.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    # Test to validate the get_google_id() method
    # Epected result is that the google_id 'google_id_583589498278432' is returned from the method
    def test_get_google_id(self):

        restaurant = Restaurant.objects.get(id=1)
        google_id = restaurant.get_google_id()
        correct_google_id = "google_id_583589498278432"
        self.assertEqual(google_id, correct_google_id)

    # Test to validate the get_longitude() method
    # Epected result is that the longitude 43.78 is returned from the method
    def test_get_longitude(self):

        restaurant = Restaurant.objects.get(id=1)
        longitude = restaurant.get_longitude()
        correct_longitude = 43.78
        self.assertEqual(longitude, correct_longitude)

    # Test to validate the get_longitude() method is not rounding number
    # Epected result is that the longitude 43.78 is returned from the method which is not equal to 44
    def test_get_longitude_fail_case(self):

        restaurant = Restaurant.objects.get(id=1)
        longitude = restaurant.get_longitude()
        correct_longitude = 44
        self.assertNotEqual(longitude, correct_longitude)

    # Test to validate the get_latitude() method
    # Epected result is that the latitude 17.35 is returned from the method
    def test_get_latitude(self):

        restaurant = Restaurant.objects.get(id=1)
        latitude = restaurant.get_latitude()
        correct_latitude = 17.35
        self.assertEqual(latitude, correct_latitude)

    # Test to validate the get_latitude() method is not rounding number
    # Epected result is that the latitude 17.35 is returned from the method which is not equal to 17
    def test_get_latitude_fail_case(self):

        restaurant = Restaurant.objects.get(id=1)
        latitude = restaurant.get_latitude()
        correct_latitude = 17
        self.assertNotEqual(latitude, correct_latitude)

    # Test to validate the get_location() method
    # Expected result is that the tuple (43.78, 17.35) is returned from the method
    def test_get_location(self):

        restaurant = Restaurant.objects.get(id=1)
        location = restaurant.get_location()
        correct_location = (43.78, 17.35)
        self.assertEqual(location, correct_location)

    # Test to validate the get_name() method
    # Expected result is that the name "A Pizza Place" is returned from the method
    def test_get_name(self):

        restaurant = Restaurant.objects.get(id=1)
        name = restaurant.get_name()
        correct_name = "A Pizza Place"
        self.assertEqual(name, correct_name)

    # Test to validate the get_address() method
    # Expected result is that the address 'Dublin' is returned from the method
    def test_get_address(self):

        restaurant = Restaurant.objects.get(id=1)
        address = restaurant.get_address()
        correct_address = 'Dublin'
        self.assertEqual(address, correct_address)

    # Test to validate the get_type() method
    # Expected result is that the type 'pizza' is returned from the method
    def test_get_type(self):

        restaurant = Restaurant.objects.get(id=1)
        type = restaurant.get_type()
        correct_type = 'pizza'
        self.assertEqual(type, correct_type)

    # Test to validate the get_price_level() method
    # Expected result is that the price_level 'PRICE_LEVEL_INEXPENSIVE' is returned from the method
    def test_get_price_level(self):

        restaurant = Restaurant.objects.get(id=1)
        price_level = restaurant.get_price_level()
        correct_price_level = 'PRICE_LEVEL_INEXPENSIVE'
        self.assertEqual(price_level, correct_price_level)

    # Test to validate the get_allows_dogs() method
    # Expected result is that the boolean True is returned from the method
    def test_get_allows_dogs(self):

        restaurant = Restaurant.objects.get(id=1)
        allows_dogs = restaurant.get_allows_dogs()
        correct_allows_dogs = True
        self.assertEqual(allows_dogs, correct_allows_dogs)

    # Test to validate the get_delivery() method
    # Expected result is that the boolean False is returned from the method
    def test_get_delivery(self):

        restaurant = Restaurant.objects.get(id=1)
        delivery = restaurant.get_delivery()
        correct_delivery = False
        self.assertEqual(delivery, correct_delivery)

    # Test to validate the get_dine_in() method
    # Expected result is that the boolean True is returned from the method
    def test_get_dine_in(self):

        restaurant = Restaurant.objects.get(id=1)
        dine_in = restaurant.get_dine_in()
        correct_dine_in = True
        self.assertEqual(dine_in, correct_dine_in)

    # Test to validate the get_good_for_children() method
    # Expected result is that the boolean True is returned from the method
    def test_get_good_for_children(self):

        restaurant = Restaurant.objects.get(id=1)
        good_for_children = restaurant.get_good_for_children()
        correct_good_for_children = True
        self.assertEqual(good_for_children, correct_good_for_children)

    # Test to validate the get_good_for_groups() method
    # Expected result is that the boolean False is returned from the method
    def test_get_good_for_groups(self):

        restaurant = Restaurant.objects.get(id=1)
        good_for_groups = restaurant.get_good_for_groups()
        correct_good_for_groups = False
        self.assertEqual(good_for_groups, correct_good_for_groups)

    # Test to validate the get_outdoor_seating() method
    # Expected result is that the boolean False is returned from the method
    def test_get_outdoor_seating(self):

        restaurant = Restaurant.objects.get(id=1)
        outdoor_seating = restaurant.get_outdoor_seating()
        correct_outdoor_seating = False
        self.assertEqual(outdoor_seating, correct_outdoor_seating)

    # Test to validate the get_hours() method
    # Expected result is that the restaurant_hours instance is returned from the method
    def test_get_hours(self):

        restaurant = Restaurant.objects.get(id=1)
        hours = restaurant.get_hours()
        correct_hours = RestaurantHours.objects.get(id=1)
        self.assertEqual(hours, correct_hours)

    # Test to validate the get_categories() method
    # Expected result is that no categories will be returned from the method, as we will delete the join instances
    def test_get_categories_empty(self):

        RestaurantCategory.objects.all().delete()
        restaurant = Restaurant.objects.get(id=1)
        categories = restaurant.get_categories()
        category_names = [category.get_category() for category in categories]
        correct_categories = []
        self.assertEqual(category_names, correct_categories)


    # Test to validate the get_categories() method
    # Expected result is that categories will be returned from the method, as we have all the join instances
    def test_get_categories_full(self):

        restaurant = Restaurant.objects.get(id=1)
        categories = restaurant.get_categories()
        category_names = [category.get_category() for category in categories]
        correct_categories = ["Chinese", "Indian"]
        self.assertEqual(category_names, correct_categories)

    # Test to validate the get_average_rating() method
    # Expected result is that no average_rating will be returned from the method, as we will delete the Review instances
    def test_get_average_rating_empty(self):

        Review.objects.all().delete()
        restaurant = Restaurant.objects.get(id=1)
        average_rating = restaurant.get_average_rating()
        correct_average_rating = 0
        self.assertEqual(average_rating, correct_average_rating)

    # Test to validate the get_average_rating() method
    # Expected result is that average_rating will be returned as 3.0, as we will have the review instances
    def test_get_average_rating_full(self):

        restaurant = Restaurant.objects.get(id=1)
        average_rating = restaurant.get_average_rating()
        correct_average_rating = 3
        self.assertEqual(average_rating, correct_average_rating)

    # Test to validate the debug_string() method
    # Expected result is f'ID: 1\nGoogle ID: google_id_583589498278432\nLocation: (43.78, 17.35)\nName: A Pizza Place\nAverage Rating: 3.0' will be returned
    def test_debug_string(self):

        restaurant = Restaurant.objects.get(id=1)
        debug_format = restaurant.debug_string()
        correct_debug_format = f'ID: 1\nGoogle ID: google_id_583589498278432\nLocation: (43.78, 17.35)\nName: A Pizza Place\nAverage Rating: 3.0'
        self.assertEqual(debug_format, correct_debug_format)

    # Test to validate the __str__() method
    # Expected result is that "A Pizza Place" is returned from the method
    def test_to_string(self):

        restaurant = Restaurant.objects.get(id=1)
        to_string = str(restaurant)
        correct_to_string = "A Pizza Place"
        self.assertEqual(to_string, correct_to_string)

# Unit tests for the Review class
class ReviewMethodTests(TestCase):

    # Initial set up of data
    # Creates 1 instance of the class APIUser
    # Creates 1 instance of the class Restaurant
    # Creates 1 instance of the class Review
    def setUpTestData():

        APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

        user = APIUser.objects.get(id=1)

        Restaurant.objects.create(
            google_id='google_id_583589498278432',
            longitude=43.78,
            latitude=17.35,
            name='A Pizza Place',
            average_rating=0,
        )

        restaurant = Restaurant.objects.get(id=1)
      
        Review.objects.create(
            user=user,
            restaurant=restaurant,
            rating=1,
            description='I had a great time :).'
        )

    # Test to validate the get_id() method
    # Expected result is that the id 1 is returned from the method
    def test_get_id(self):

        review = Review.objects.get(id=1)
        id = review.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    # Test to validate the get_user() method
    # Expected result is that the user created is returned from the method
    def test_get_user(self):

        review = Review.objects.get(id=1)
        user = review.get_user()
        correct_user = APIUser.objects.get(id=1)
        self.assertEqual(user, correct_user)

    # Test to validate the get_restaurant() method
    # Expected result is that the restaurant created is returned from the method
    def test_get_restaurant(self):

        review = Review.objects.get(id=1)
        restaurant = review.get_restaurant()
        correct_restaurant = Restaurant.objects.get(id=1)
        self.assertEqual(restaurant, correct_restaurant)

    # Test to validate the get_rating() method
    # Expected result is that the rating is returned from the method
    def test_get_rating(self):

        review = Review.objects.get(id=1)
        rating = review.get_rating()
        correct_rating = 1
        self.assertEqual(rating, correct_rating)

    # Test to validate the get_description() method
    # Expected result is that the description is returned from the method
    def test_get_description(self):

        review = Review.objects.get(id=1)
        description = review.get_description()
        correct_description = "I had a great time :)."
        self.assertEqual(description, correct_description)

    # Test to validate the get_description() method
    # Expected result is that the description is returned from the method
    def test_debug_string(self):

        review = Review.objects.get(id=1)
        debug_format = review.debug_string()
        correct_debug_format = f'ID: 1\nUser: dalye54\nRestaurant: A Pizza Place\nRating: 1\nDescription: I had a great time :).'
        self.assertEqual(debug_format, correct_debug_format)

    # Test to validate the __str__() method
    # Expected result is that "dalye54 -- A Pizza Place: 1" is returned from the method
    def test_to_string(self):

        review = Review.objects.get(id=1)
        to_string = str(review)
        correct_to_string = "dalye54 -- A Pizza Place: 1"
        self.assertEqual(to_string, correct_to_string)

# Unit tests for the Category class
class CategoryMethodTests(TestCase):

    # Initial set up of data
    # Creates 1 instance of the class Category
    def setUpTestData():

        Category.objects.create(
            category="Chinese"
        )

    # Test to validate the get_id() method
    # Expected result is that the id 1 is returned from the method
    def test_get_id(self):

        category = Category.objects.get(id=1)
        id = category.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    # Test to validate the get_category() method
    # Expected result is that the category "Chinese" is returned from the method
    def test_get_category(self):

        category = Category.objects.get(id=1)
        category = category.get_category()
        correct_category = "Chinese"
        self.assertEqual(category, correct_category)

    # Test to validate the debug_string() method
    # Expected result is f'ID: 1\nCategory: Chinese' will be returned
    def test_debug_string(self):

        category = Category.objects.get(id=1)
        debug_format = category.debug_string()
        correct_debug_format = f'ID: 1\nCategory: Chinese'
        self.assertEqual(debug_format, correct_debug_format)

    # Test to validate the to_string() method
    # Expected result is "Chinese" will be returned
    def test_to_string(self):

        category = Category.objects.get(id=1)
        to_string = str(category)
        correct_to_string = "Chinese"
        self.assertEqual(to_string, correct_to_string)

# Unit tests for the RestaurantCategory class
class RestaurantCategoryTests(TestCase):

    # Initial set up of data
    # Creates 1 instance of the class Restaurant
    # Creates 1 instance of the class Category
    # Creates 1 instance of the class RestaurantCategory
    def setUpTestData():

        Restaurant.objects.create(
            google_id='google_id_583589498278432',
            longitude=43.78,
            latitude=17.35,
            name='A Pizza Place',
            average_rating=0,
        )

        restaurant = Restaurant.objects.get(id=1)

        Category.objects.create(
            category='Chinese'
        )

        category = Category.objects.get(id=1)

        RestaurantCategory.objects.create(

            category=category,
            restaurant=restaurant,
        )

    # Test to validate the get_id() method
    # Expected result is that the id 1 is returned from the method
    def test_get_id(self):

        restaurantcategory = RestaurantCategory.objects.get(id=1)
        id = restaurantcategory.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    # Test to validate the get_category() method
    # Expected result is that the category instance is returned from the method
    def test_get_category(self):

        restaurantcategory = RestaurantCategory.objects.get(id=1)
        category = restaurantcategory.get_category()
        correct_category = Category.objects.get(id=1)
        self.assertEqual(category, correct_category)

    # Test to validate the get_restaurant() method
    # Expected result is that the restaurant instance is returned from the method
    def test_get_restaurant(self):

        restaurantcategory = RestaurantCategory.objects.get(id=1)
        restaurant = restaurantcategory.get_restaurant()
        correct_restaurant = Restaurant.objects.get(id=1)
        self.assertEqual(restaurant, correct_restaurant)

    # Test to validate the debug_string() method
    # Expected result is that the full_name f'ID: 1\nCategory: Chinese\nRestaurant: A Pizza Place' is returned from the method
    def test_debug_string(self):

        restaurantcategory = RestaurantCategory.objects.get(id=1)
        debug_format = restaurantcategory.debug_string()
        correct_debug_format = f'ID: 1\nCategory: Chinese\nRestaurant: A Pizza Place'
        self.assertEqual(debug_format, correct_debug_format)

    # Test to validate the __str__() method
    # Expected result is that 'Chinese -- A Pizza Place' is returned from the method
    def test_to_string(self):

        restaurantcategory = RestaurantCategory.objects.get(id=1)
        to_string = str(restaurantcategory)
        correct_to_string = "Chinese -- A Pizza Place"
        self.assertEqual(to_string, correct_to_string)

# Restaurant Time
class RestaurantTimeMethodTests(TestCase):

    # Initial set up of data
    # Creates 1 instance of the class RestaurantTime
    def setUpTestData():

        RestaurantTime.objects.create(
            hour=12,
            minute=30
        )

    # Test to validate the get_id() method
    # Expected result is that the id 1 is returned from the method
    def test_get_id(self):

        restauranttime = RestaurantTime.objects.get(id=1)
        id = restauranttime.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    # Test to validate the get_hour() method
    # Expected result is that the hour 12 is returned from the method
    def test_get_hour(self):

        restauranttime = RestaurantTime.objects.get(id=1)
        hour = restauranttime.get_hour()
        correct_hour = 12
        self.assertEqual(hour, correct_hour)

    # Test to validate the get_minute() method
    # Expected result is that the minute 30 is returned from the method
    def test_get_minute(self):

        restauranttime = RestaurantTime.objects.get(id=1)
        minute = restauranttime.get_minute()
        correct_minute = 30
        self.assertEqual(minute, correct_minute)

    # Test to validate the __str__() method
    # Expected result is that '12:30' is returned from the method
    def test_to_string(self):

        restauranttime = RestaurantTime.objects.get(id=1)
        to_string = str(restauranttime)
        correct_to_string = '12:30'
        self.assertEqual(to_string, correct_to_string)

# Unit tests for the RestaurantDay class
class RestaurantDayMethodTests(TestCase):

    # Initial set up of data
    # Creates 2 instances of the class RestaurantTime
    # Creates 2 instance of the class RestaurantDay
    def setUpTestData():

        RestaurantTime.objects.create(
            hour=12,
            minute=30
        )

        restauranttime_open = RestaurantTime.objects.get(id=1)

        RestaurantTime.objects.create(
            hour=18,
            minute=45
        )

        restauranttime_close = RestaurantTime.objects.get(id=2)

        RestaurantDay.objects.create(
            open=True,
            open_time=restauranttime_open,
            close_time=restauranttime_close
        )

        RestaurantDay.objects.create(
            open=False
        )

    # Test to validate the get_id() method
    # Expected result is that the id 1 is returned from the method on the open RestaurantDay instance
    def test_get_id_open(self):

        restaurantday_open = RestaurantDay.objects.get(id=1)
        id = restaurantday_open.get_id()
        correct_id = 1
        self.assertEqual(id, correct_id)

    # Test to validate the get_id() method
    # Expected result is that the id 2 is returned from the method on the closed RestaurantDay instance
    def test_get_id_closed(self):

        restaurantday_closed = RestaurantDay.objects.get(id=2)
        id = restaurantday_closed.get_id()
        correct_id = 2
        self.assertEqual(id, correct_id)

    # Test to validate the get_open() method
    # Expected result is that the boolean True is returned from the method on the open RestaurantDay instance
    def test_get_open_open(self):

        restaurantday_open = RestaurantDay.objects.get(id=1)
        open = restaurantday_open.get_open()
        correct_open = True
        self.assertEqual(open, correct_open)

    # Test to validate the get_open() method
    # Expected result is that the boolean False is returned from the method on the closed RestaurantDay instance
    def test_get_open_closed(self):

        restaurantday_closed = RestaurantDay.objects.get(id=2)
        open = restaurantday_closed.get_open()
        correct_open = False
        self.assertEqual(open, correct_open)

    # Test to validate the get_open_time() method
    # Expected result is that the instance of RestaurantTime is returned from the method on the open RestaurantDay instance
    def test_get_open_time_open(self):

        restaurantday_open = RestaurantDay.objects.get(id=1)
        open_time = restaurantday_open.get_open_time()
        correct_open_time = RestaurantTime.objects.get(id=1)
        self.assertEqual(open_time, correct_open_time)

    # Test to validate the get_open_time() method
    # Expected result is that None is returned from the method on the closed RestaurantDay instance
    def test_get_open_time_closed(self):

        restaurantday_closed = RestaurantDay.objects.get(id=2)
        open_time = restaurantday_closed.get_open_time()
        correct_open_time = None
        self.assertEqual(open_time, correct_open_time)

    # Test to validate the get_close_time() method
    # Expected result is that the instance of RestaurantTime is returned from the method on the open RestaurantDay instance
    def test_get_close_time_open(self):

        restaurantday_open = RestaurantDay.objects.get(id=1)
        close_time = restaurantday_open.get_close_time()
        correct_close_time = RestaurantTime.objects.get(id=2)
        self.assertEqual(close_time, correct_close_time)

    # Test to validate the get_close_time() method
    # Expected result is that None is returned from the method on the closed RestaurantDay instance
    def test_get_close_time_close(self):

        restaurantday_closed = RestaurantDay.objects.get(id=2)
        close_time = restaurantday_closed.get_open_time()
        correct_close_time = None
        self.assertEqual(close_time, correct_close_time)

    # Test to validate the __str__() method
    # Expected result is that '12:30 - 18:45' is returned from the method
    def test_to_string_open(self):

        to_string = str(RestaurantDay.objects.get(id=1))
        correct_to_string = '12:30 - 18:45'
        self.assertEqual(to_string, correct_to_string)

    # Test to validate the __str__() method
    # Expected result is that 'Closed' is returned from the method
    def test_to_string_closed(self):

        to_string = str(RestaurantDay.objects.get(id=2))
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
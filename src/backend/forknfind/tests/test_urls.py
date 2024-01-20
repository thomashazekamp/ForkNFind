from rest_framework.test import APIClient, APITestCase
from ..views import *
from ..models import *
import random
from django.core.exceptions import ObjectDoesNotExist
from unittest import mock
from ..requests import google_maps_nearby_search

# Unit tests for the Register User API
class APIRegisterUserTests(APITestCase):

    # Needed as after a user's account is created the recommender updates for that new user
    # Initial set up of data
    # Creates 1 instance of the class HybridRecommender 
    # Creates 20 instances of the class APIUser
    # Creates 20 instances of the class Restaurant
    # Creates 100 instances of the class Review
    # Creates 1 instance of the class RestaurantDay
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

# Unit tests for the Register Review API
class APIRegisterReviewTests(APITestCase):

    # Initial set up of data
    # Creates 1 instances of the class APIUser
    # Creates 1 instances of the class Restaurant
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
    def setUpTestData():

        APIUser.objects.create(
            username='dalye54',
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

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):

        self.client = APIClient()

    def test_post_api_register_review(self):

        # get the user we will be logging into
        user = APIUser.objects.get(id=1)

        # data to create new review
        self.client.force_authenticate(user=user)

        # data to create new review
        data = {"restaurant": "1", "rating": "4", "description": "Was a really good time and i enjoyed my food a lot."}

        # post the data to the url in json format
        response = self.client.post("/register/review/", data=data, format="json")

        # verify the response data has been created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get the created user
        review = Review.objects.get(id=1)

        # verify the data in the review is the same as what we sent
        self.assertEqual(review.get_user(), user)
        self.assertEqual(review.get_restaurant(), Restaurant.objects.get(id=1))
        self.assertEqual(review.get_rating(), int(data['rating']))
        self.assertEqual(review.get_description(), data['description'])

# Unit tests for the Recommend Restaurant Content API
class APIRegisterReviewTests(APITestCase):

    # Initial set up of data
    # Creates 1 instance of the class HybridRecommender 
    # Initialise the HybridRecommender
    # Creates 20 instances of the class APIUser
    # Creates 20 instances of the class Restaurant
    # Creates 100 instances of the class Review
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
    # Creates 2 instances of the class Category
    # Creates 2 instances of the class RestaurantCategory
    def setUpTestData():

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

        HybridRecommender.objects.create()

        # Get the instance of the hybridrecommender
        hybridrecommender = HybridRecommender.objects.get(id=1)

        # Start the recommender
        hybridrecommender.start_recommender()

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):

        self.client = APIClient()

    # Testing the API
    # Expected result is three valid restaurant id's being returned in a list
    def test_get_api_content_recommendation(self):

        # send a get request for data
        response = self.client.get("/recommend/content/1/53.580041/-6.107879/", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 3 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 3)

        for item in data:

            try:
                Restaurant.objects.get(id=item['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {item['id']}")

# Unit tests for the Recommend Restaurant Collaborative API
class APIRecommendRestaurantCollaborativeTests(APITestCase):

    # Initial set up of data
    # Creates 1 instance of the class HybridRecommender 
    # Initialise the HybridRecommender
    # Creates 20 instances of the class APIUser
    # Creates 20 instances of the class Restaurant
    # Creates 100 instances of the class Review
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
    # Creates 2 instances of the class Category
    # Creates 2 instances of the class RestaurantCategory
    def setUpTestData():

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

        HybridRecommender.objects.create()

        # Get the instance of the hybridrecommender
        hybridrecommender = HybridRecommender.objects.get(id=1)

        # Start the recommender
        hybridrecommender.start_recommender()

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):

        self.client = APIClient()

    # Testing the API
    # Expected result is three valid restaurant id's being returned in a list
    def test_get_api_collaborative_recommendation(self):

        # get the user we will be logging into
        user = APIUser.objects.get(id=1)

        # set the login user
        self.client.force_authenticate(user=user)

        # send a get request for data
        response = self.client.get("/recommend/collaborative/", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 3 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 3)

        for id in data:

            try:
                Restaurant.objects.get(id=id)
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {id}")

# Unit tests for the Recommend Restaurant Hybrid API
class APIRecommendRestaurantHybridTests(APITestCase):

    # Initial set up of data
    # Creates 1 instance of the class HybridRecommender 
    # Initialise the HybridRecommender
    # Creates 20 instances of the class APIUser
    # Creates 20 instances of the class Restaurant
    # Creates 100 instances of the class Review
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
    # Creates 2 instances of the class Category
    # Creates 2 instances of the class RestaurantCategory
    def setUpTestData():

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

        HybridRecommender.objects.create()

        # Get the instance of the hybridrecommender
        hybridrecommender = HybridRecommender.objects.get(id=1)

        # Start the recommender
        hybridrecommender.start_recommender()

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):

        self.client = APIClient()

    # Testing the API
    # Expected result is three valid restaurant id's being returned in a list
    def test_get_api_hybrid_recommendation(self):

        # get the user we will be logging into
        user = APIUser.objects.get(id=1)

        # set the login user
        self.client.force_authenticate(user=user)

        # send a get request for data
        response = self.client.get("/recommend/hybrid/53.580041/-6.107879/", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with items
        self.assertEqual(type(data), list)

        for item in data:

            try:
                Restaurant.objects.get(id=item['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {item['id']}")


# Unit tests for the Searching Restaurants API
class APISearchRestaurantTests(APITestCase):

    # Initial set up of data
    # Creates 4 instances of the class Restaurant
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
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

        # Create 4 unique restaurants with these attributes and link them to the categories with id 1 and 2
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
            average_rating=3,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583589498478432',
            longitude=43.78,
            latitude=17.35,
            name='A Pasta Place',
            address='Cork',
            type='pasta',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=True, 
            dine_in=False, 
            good_for_children=False,
            good_for_groups=True,
            outdoor_seating=True,
            average_rating=4,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583583498278432',
            longitude=43.78,
            latitude=17.35,
            name='A Chinese Place',
            address='Belfast',
            type='chinese',
            price_level='PRICE_LEVEL_INEXPENSIVE',
            allows_dogs=True,
            delivery=True,
            dine_in=False,
            good_for_children=False,
            good_for_groups=True,
            outdoor_seating=True,
            average_rating=1,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583589198278432',
            longitude=43.78,
            latitude=17.35,
            name='Apache Pizza',
            address='Donegal',
            type='pizza',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=False,
            dine_in=True,
            good_for_children=True,
            good_for_groups=False,
            outdoor_seating=False,
            average_rating=5,
            hours=restaurant_hours
        )

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):
        self.client = APIClient()

    # Testing search functionality using the names of restaurants
    # Expected result is three restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_name_parameter(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?name=place", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 3 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 3)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the names of restaurants
    # Expected result is three restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_name_parameter(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?name=place", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 3 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 3)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the addresses of restaurants
    # Expected result is one restaurants is returned from search and the id is checked against the database
    def test_search_restaurant_address_parameter(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?address=dublin", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 1 item
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the type of restaurants
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_type_parameter(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?type=pizza", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the price level of restaurants
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_price_level_parameter(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?price_level=PRICE_LEVEL_MODERATE", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the allow dogs of restaurants, value inputted false
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_allow_dogs_parameter_false(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?allows_dogs=false", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the allow dogs of restaurants, value inputted true
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_allow_dogs_parameter_true(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?allows_dogs=true", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the delivery of restaurants, value inputted false
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_delivery_parameter_false(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?delivery=false", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the delivery of restaurants, value inputted true
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_delivery_parameter_true(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?delivery=true", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the dine in of restaurants, value inputted false
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_dine_in_parameter_false(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?dine_in=false", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the dine in of restaurants, value inputted true
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_dine_in_parameter_true(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?dine_in=true", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the good for children of restaurants, value inputted false
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_good_for_children_parameter_false(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?good_for_children=false", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the good for children of restaurants, value inputted true
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_good_for_children_parameter_true(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?good_for_children=true", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the good for groups of restaurants, value inputted false
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_good_for_groups_parameter_false(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?good_for_groups=false", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the good for groups of restaurants, value inputted true
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_good_for_groups_parameter_true(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?good_for_groups=true", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the outdoor seating of restaurants, value inputted false
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_outdoor_seating_parameter_false(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?outdoor_seating=false", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the outdoor seating of restaurants, value inputted true
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_outdoor_seating_parameter_true(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?outdoor_seating=true", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

    # Testing search functionality using the average rating of restaurants
    # Expected result is two restaurants are returned from search and their id's are checked against the database
    def test_search_restaurant_average_rating_parameter_true(self):
        
        # send a get request for data
        response = self.client.get("/search/restaurant/53.580041/-6.107879/?average_rating=4", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 2 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 2)

        for line in data:

            try:
                Restaurant.objects.get(id=line['id'])
            except ObjectDoesNotExist:
                self.fail(f"API broken: Failed with ID {line['id']}")

# Unit tests for the Getting User Reviews API
class APIReviewUserTests(APITestCase):

    # Initial set up of data
    # Creates 3 instance of the class APIUser
    # Creates 2 instances of the class Restaurant
    # Creates 2 instances of the class Review
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
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
            average_rating=3,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583589498478432',
            longitude=43.78,
            latitude=17.35,
            name='A Pasta Place',
            address='Cork',
            type='pasta',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=True, 
            dine_in=False, 
            good_for_children=False,
            good_for_groups=True,
            outdoor_seating=True,
            average_rating=4,
            hours=restaurant_hours
        )

        APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

        APIUser.objects.create(
            username='johndoe',
            first_name='john',
            last_name='doe',
            email='john.doe@mail.dcu.ie',
            password='password'
        )

        APIUser.objects.create(
            username='no_review',
            first_name='no',
            last_name='review',
            email='no.review@mail.dcu.ie',
            password='password'
        )

        Review.objects.create(
            user=APIUser.objects.get(id=1),
            restaurant=Restaurant.objects.get(id=1),
            rating=5,
            description="Nice restaurant"   
        )

        Review.objects.create(
            user=APIUser.objects.get(id=2),
            restaurant=Restaurant.objects.get(id=2),
            rating=1,
            description="Not nice restaurant"   
        )

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):
        self.client = APIClient()

    # Testing getting the reviews made by a given user
    # Expected result is 1 review is returned as the user has only made 1 review in the database
    def test_get_active_user_reviews(self):

         # get the user we will be logging into
        user = APIUser.objects.get(id=1)

        # set the login user
        self.client.force_authenticate(user=user)

        # send a get request for data
        response = self.client.get("/review/user/", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 1 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)

        # check the review has same id as the one we created in setupdata
        self.assertEqual(data[0]['id'], 1)

    # Testing getting the reviews made by a given user, if they have made 0 reviews
    # Expected result is no reviews are returned as the user has yet to make one
    def test_get_active_user_reviews_if_no_review_has_been_made_for_user(self):

         # get the user we will be logging into
        user = APIUser.objects.get(id=3)

        # set the login user
        self.client.force_authenticate(user=user)

        # send a get request for data
        response = self.client.get("/review/user/", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 0 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 0)

# Unit tests for the Getting Restaurant Reviews API
class APIReviewRestaurantTests(APITestCase):

    # Initial set up of data
    # Creates 2 instance of the class APIUser
    # Creates 3 instances of the class Restaurant
    # Creates 2 instances of the class Review
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
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
            average_rating=3,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583589498478432',
            longitude=43.78,
            latitude=17.35,
            name='A Pasta Place',
            address='Cork',
            type='pasta',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=True, 
            dine_in=False, 
            good_for_children=False,
            good_for_groups=True,
            outdoor_seating=True,
            average_rating=4,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583589198278432',
            longitude=43.78,
            latitude=17.35,
            name='Apache Pizza',
            address='Donegal',
            type='pizza',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=False,
            dine_in=True,
            good_for_children=True,
            good_for_groups=False,
            outdoor_seating=False,
            average_rating=5,
            hours=restaurant_hours
        )

        APIUser.objects.create(
            username='dalye54',
            first_name='Eoin',
            last_name='Daly',
            email='eoin.daly54@mail.dcu.ie',
            password='password'
        )

        APIUser.objects.create(
            username='johndoe',
            first_name='john',
            last_name='doe',
            email='john.doe@mail.dcu.ie',
            password='password'
        )

        Review.objects.create(
            user=APIUser.objects.get(id=1),
            restaurant=Restaurant.objects.get(id=1),
            rating=5,
            description="Nice restaurant"   
        )

        Review.objects.create(
            user=APIUser.objects.get(id=2),
            restaurant=Restaurant.objects.get(id=2),
            rating=1,
            description="Not nice restaurant"   
        )

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):
        self.client = APIClient()

    # Testing getting the reviews made for a given restaurant
    # Expected result is 1 review is returned as the restaurant has only 1 review in the database
    def test_get_specified_restaurant_reviews(self):

        # send a get request for data
        response = self.client.get("/review/restaurant/1/", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 1 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)

        # check the review has same id as the one we created in setupdata
        self.assertEqual(data[0]['id'], 1)

    # Testing getting the reviews made for a given restaurant
    # Expected result is no reviews are returned as restaurant has yet to receive one
    def test_get_specified_restaurant_reviews_if_no_review_has_been_made_for_restaurant(self):

        # send a get request for data
        response = self.client.get("/review/restaurant/3/", format="json")

        # verify the response data is ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that a list is returned with 0 items
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 0)

# Mocked the external API call to the Google services
def google_maps_nearby_search_mock(tmp, tmp2):
    return {"places": [
            {"id": "google_id_583589498278432", "displayName": {"text": "A Pizza Place", "languageCode": "en"}},
            {"id": "google_id_583589498478432", "displayName": {"text": "A Pasta Place", "languageCode": "en"}},
            {"id": "google_id_583583498278432", "displayName": {"text": "A Chinese Place", "languageCode": "en"}},
            {"id": "google_id_583589198278432", "displayName": {"text": "Apache Pizza", "languageCode": "en"}},
            {"id": "google_id_5835986198278432", "displayName": {"text": "Apache Pizza", "languageCode": "en"}},
        ]}


# Unit tests for the Find Restaurants API
class APIFindRestaurantsTests(APITestCase):

    # Initial set up of data
    # Creates 5 instances of the class Restaurant
    # Creates 1 instance of the class RestaurantDay
    # Creates 1 instance of the class RestaurantHours
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

        # Create 5 unique restaurants with these attributes and link them to the categories with id 1 and 2
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
            average_rating=3,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583589498478432',
            longitude=43.78,
            latitude=17.35,
            name='A Pasta Place',
            address='Cork',
            type='pasta',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=True, 
            dine_in=False, 
            good_for_children=False,
            good_for_groups=True,
            outdoor_seating=True,
            average_rating=4,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583583498278432',
            longitude=43.78,
            latitude=17.35,
            name='A Chinese Place',
            address='Belfast',
            type='chinese',
            price_level='PRICE_LEVEL_INEXPENSIVE',
            allows_dogs=True,
            delivery=True,
            dine_in=False,
            good_for_children=False,
            good_for_groups=True,
            outdoor_seating=True,
            average_rating=1,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_583589198278432',
            longitude=60.78,
            latitude=17.35,
            name='Apache Pizza',
            address='Donegal',
            type='pizza',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=False,
            dine_in=True,
            good_for_children=True,
            good_for_groups=False,
            outdoor_seating=False,
            average_rating=5,
            hours=restaurant_hours
        )

        Restaurant.objects.create(
            google_id='google_id_5835986198278432',
            longitude=60.78,
            latitude=17.35,
            name='Apache Pizza',
            address='Mayo',
            type='pizza',
            price_level='PRICE_LEVEL_MODERATE',
            allows_dogs=False,
            delivery=False,
            dine_in=True,
            good_for_children=True,
            good_for_groups=False,
            outdoor_seating=False,
            average_rating=4,
            hours=restaurant_hours
        )

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):
        self.client = APIClient()

    # Testing finding restaurants within 2km of user
    # Expected result is 3 restaurants will be returned as they are within the distance
    # Mocking function so when it is called it goes to the mocked function skipping the google request
    @mock.patch('forknfind.requests.google_maps_nearby_search', side_effect=google_maps_nearby_search_mock)
    def test_find_restaurants_nearby(self, _):

        # data of user location
        data = {"longitude": 43.78, "latitude": 17.35}

        # post the data to the url in json format
        response = self.client.post("/find/restaurants/", data=data, format="json")

        # verify the response data has been created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        
        # verify that a dict is returned with 3 items
        self.assertEqual(type(data), dict)
        self.assertEqual(len(data), 3)

    # Testing finding restaurants within 2km of user
    # Expected result is 0 restaurants will be returned as no restaurants will be within range
    # Mocking function so when it is called it goes to the mocked function skipping the google request
    @mock.patch('forknfind.requests.google_maps_nearby_search', side_effect=google_maps_nearby_search_mock)
    def test_find_restaurants_nearby(self, _):

        # data of user location
        data = {"longitude": 43.78, "latitude": 19.35}

        # post the data to the url in json format
        response = self.client.post("/find/restaurants/", data=data, format="json")

        # verify the response data has been created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        
        # verify that a dict is returned with 3 items
        self.assertEqual(type(data), dict)
        self.assertEqual(len(data), 0)

# Unit tests for the Getting User Reviews API
class APIReviewUserTests(APITestCase):

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

    # Set up data for each test
    # Creates 1 instances of the APIClient
    def setUp(self):
        self.client = APIClient()

    # Testing changing a password for a user
    # Expected result is for it to fail as we are sending the incorrect current password
    def test_incorrect_password_change_request(self):

        # get the user we will be logging into
        user = APIUser.objects.get(id=1)

        # set the login user
        self.client.force_authenticate(user=user)

        # data to be sent
        data = {"current_password": "test", "new_password": "newpassword"}

        # send a get request for data
        response = self.client.post("/user/password/update/", data=data, format="json")

        # verify the response data is an error
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = response.json()

        # verify that the response data is an error
        self.assertEqual(data, {'error': 'Incorrect password'})

    # Testing changing a password for a user
    # Expected result is for it to succeed as we are sening the correct current password
    def test_success_password_change_request(self):

        # get the user we will be logging into
        user = APIUser.objects.get(id=1)

        # set the login user
        self.client.force_authenticate(user=user)

        # data to be sent
        post_data = {"current_password": "password", "new_password": "test"}

        # send a get request for data
        response = self.client.post("/user/password/update/", data=post_data, format="json")

        # verify the response data is an error
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        # verify that the response data is an error
        self.assertEqual(data, {'detail': 'Success'})

        # verify the new password has been updated
        user = APIUser.objects.get(id=1)
        self.assertTrue(user.check_password(post_data['new_password']))
from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters
from .formula import *
from datetime import datetime, time

# UserSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] # Show these fields

# ReviewSerializer
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user','restaurant','rating','description'] # Show these fields

# CategorySerializer
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category'] # Show these fields

# RestaurantCategorySerializer
class RestaurantCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantCategory
        fields = ['id', 'restaurant', 'category'] # Show these fields

# RestaurantTimeSerializer
class RestaurantTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantTime
        fields = ['hour','minute'] # Show these fields

# RestaurantDaySerializer
class RestaurantDaySerializer(serializers.HyperlinkedModelSerializer):
    # include the serializers of these instances so all the information is shown
    open_time = RestaurantTimeSerializer()
    close_time = RestaurantTimeSerializer()

    class Meta:
        model = RestaurantDay
        fields = ['open','open_time','close_time'] # Show these fields

# RestaurantHoursSerializer
class RestaurantHoursSerializer(serializers.HyperlinkedModelSerializer):
    # include the serializers of these instances so all the information is shown
    monday = RestaurantDaySerializer()
    tuesday = RestaurantDaySerializer()
    wednesday = RestaurantDaySerializer()
    thursday = RestaurantDaySerializer()
    friday = RestaurantDaySerializer()
    saturday = RestaurantDaySerializer()
    sunday = RestaurantDaySerializer()

    class Meta:
        model = RestaurantHours
        fields = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday'] # Show these fields

# RestaurantSerializer
class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    # include the serializer of this instance so all the information is shown
    hours = RestaurantHoursSerializer()

    class Meta:
        model = Restaurant
        fields = ['id','google_id','longitude','latitude','name','address','type','price_level','allows_dogs','delivery','dine_in','good_for_children','good_for_groups','outdoor_seating', 'hours', 'average_rating'] # Show these fields

# UserRegistrationSerializer
class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = APIUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password'] # Show these fields
        extra_kwargs = {'password': {'write_only': True}}

    # for creating a new user
    def create(self, validated_data):

        # extract all the data
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        username = validated_data['username'] 
        password = validated_data['password'] 

        # save the information about the user
        new_user = APIUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        new_user.save()

        # reload the recommender as a new user has been added
        model = HybridRecommender.load()
        model.update_collaborative_recommender()

        # return new user
        return new_user
    
# RestaurantRegistrationSerializer
class RestaurantRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['google_id','longitude','latitude','name'] # Show these fields
    
    def create(self, validated_data):

        # extract all the data
        google_id = validated_data['google_id']
        longitude = validated_data['longitude']
        latitude = validated_data['latitude'] 
        name = validated_data['name']

        # save the information about the restaurant
        new_restaurant = Restaurant.objects.create(google_id=google_id, longitude=longitude, latitude=latitude, name=name, average_rating=0)
        new_restaurant.save()

        # return new restaurant
        return new_restaurant

# ReviewRegistrationSerializer
class ReviewRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['restaurant', 'rating', 'description'] # Show these fields

    def create(self, validated_data):

        # extract the user who sent the request
        request = self.context.get('request', None)
        user = request.user

        # extract all the data
        restaurant = validated_data['restaurant']
        rating = validated_data['rating']
        description = validated_data['description']

        # save the information about the review
        new_review = Review.objects.create(user=user, restaurant=restaurant, rating=rating, description=description)
        new_review.save()

        # reload the recommender as a new review has been added
        model = HybridRecommender.load()
        model.update_collaborative_recommender()

        # return the new review
        return new_review

# SearchRestaurantFilter for the search lookup
class SearchRestaurantFilter(filters.FilterSet):

    # filters that can be used when searching
    name = filters.CharFilter(lookup_expr='icontains')
    address = filters.CharFilter(lookup_expr='icontains')
    type = filters.CharFilter(lookup_expr='icontains')
    price_level = filters.CharFilter(lookup_expr='icontains')
    allows_dogs = filters.BooleanFilter()
    delivery = filters.BooleanFilter()
    dine_in = filters.BooleanFilter()
    good_for_children = filters.BooleanFilter()
    good_for_groups = filters.BooleanFilter()
    outdoor_seating = filters.BooleanFilter()
    average_rating = filters.NumberFilter(lookup_expr='gte')

    class Meta:
        model = Restaurant
        fields = ['name','address','type','price_level','allows_dogs','delivery','dine_in','good_for_children','good_for_groups','outdoor_seating','average_rating'] # Show these fields

# Used as part of the RestaurantSearchSerializer
# Calculates whether a resturant is open or closed
def time_check_function(restaurantday):

    # check if the restaurant opens on this day
    if restaurantday.get_open() == False:
        return "Closed"

    # get the instances of RestaurantTime
    open_time = restaurantday.get_open_time()
    close_time = restaurantday.get_close_time()

    # converts to instances of Time
    open_time = time(open_time.get_hour(), open_time.get_minute())
    close_time = time(close_time.get_hour(), close_time.get_minute())

    # the current time the request has been made
    current_time = datetime.now().time()

    # check if the current time is between the open time and close time
    if open_time <= current_time <= close_time:
        return "Open"
    else:
        return "Closed"

# RestaurantSearchSerializer
class RestaurantSearchSerializer(serializers.HyperlinkedModelSerializer):
    # include additional fields of information for the instance
    distance_from_user = serializers.SerializerMethodField()
    open_or_close = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id','name','type','price_level','average_rating', 'distance_from_user', 'open_or_close'] # Show these fields

    # gets the distance from the user making the query to the restaurant
    def get_distance_from_user(self, obj):

        return haversine((float(self.context.get('latitude')),float(self.context.get('longitude'))) ,obj.get_location())

    def get_open_or_close(self, obj):
        
        # work out the current day
        current_datetime = datetime.now()
        current_day = current_datetime.weekday()

        if current_day == 0:
            return time_check_function(obj.get_hours().get_monday())
        elif current_day == 1:
            return time_check_function(obj.get_hours().get_tuesday())
        elif current_day == 2:
            return time_check_function(obj.get_hours().get_wednesday())
        elif current_day == 3:
            return time_check_function(obj.get_hours().get_thursday())
        elif current_day == 4:
            return time_check_function(obj.get_hours().get_friday())
        elif current_day == 5:
            return time_check_function(obj.get_hours().get_saturday())
        elif current_day == 6:
            return time_check_function(obj.get_hours().get_sunday())
        
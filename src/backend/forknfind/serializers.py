from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters
from .formula import *
from datetime import datetime, time
from .time_check import *

# UserSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] # Show these fields

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
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id','google_id','longitude','latitude','name','address','type','price_level','allows_dogs','delivery','dine_in','good_for_children','good_for_groups','outdoor_seating', 'hours', 'average_rating', 'categories'] # Show these fields

    # getting categories associated with restaurants
    def get_categories(self, obj):
        
        instances = obj.get_categories()

        return [item.get_category() for item in instances]

# ReviewSerializer
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = Review
        fields = ['id','user','restaurant','rating','description', 'date'] # Show these fields

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

# RestaurantSearchSerializer
class RestaurantSearchSerializer(serializers.HyperlinkedModelSerializer):
    # include additional fields of information for the instance
    distance_from_user = serializers.SerializerMethodField()
    open_or_close_value = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id','name','type','price_level','average_rating', 'distance_from_user', 'open_or_close_value'] # Show these fields

    # gets the distance from the user making the query to the restaurant
    def get_distance_from_user(self, obj):

        return haversine((float(self.context.get('latitude')),float(self.context.get('longitude'))) ,obj.get_location())

    def get_open_or_close_value(self, obj):
        
        return get_open_or_close(obj)
        
    def get_average_rating(Self, obj):
        
        return obj.get_average_rating()
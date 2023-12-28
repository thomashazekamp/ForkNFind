from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] # Show these fields

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','google_id','longitude','latitude','name','average_rating']

class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = APIUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password'] # Show these fields
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        username = validated_data['username'] 
        password = validated_data['password'] 

        new_user = APIUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        new_user.save()

        print(new_user) # For checking the register worked correctly, can be commented out.

        return new_user
    
class RestaurantRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['google_id','longitude','latitude','name']
    
    def create(self, validated_data):

        google_id = validated_data['google_id']
        longitude = validated_data['longitude']
        latitude = validated_data['latitude'] 
        name = validated_data['name']

        new_restaurant = Restaurant.objects.create(google_id=google_id, longitude=longitude, latitude=latitude, name=name, average_rating=0)
        new_restaurant.save()

        return new_restaurant
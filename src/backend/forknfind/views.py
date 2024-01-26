from .models import *
from .serializers import *
from .requests import *
from .formula import *
from .time_check import *

from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# UserViewSet, queryset of all APIUser instances
class UserViewSet(viewsets.ModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = UserSerializer

# RestaurantViewSet, queryset of all Restaurant instances
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# ReviewViewSet, queryset of all Review instances
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# CategoryViewSet, queryset of all Category instances
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# RestaurantCategoryViewSet, queryset of all RestaurantCategory instances
class RestaurantCategoryViewSet(viewsets.ModelViewSet):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer

# RestaurantTimeViewSet, queryset of all RestaurantTime instances
class RestaurantTimeViewSet(viewsets.ModelViewSet):
    queryset = RestaurantTime.objects.all()
    serializer_class = RestaurantTimeSerializer

# RestaurantDayViewSet, queryset of all RestaurantDay instances
class RestaurantDayViewSet(viewsets.ModelViewSet):
    queryset = RestaurantDay.objects.all()
    serializer_class = RestaurantDaySerializer

# RestaurantHoursViewSet, queryset of all RestaurantHours instances
class RestaurantHoursViewSet(viewsets.ModelViewSet):
    queryset = RestaurantHours.objects.all()
    serializer_class = RestaurantHoursSerializer

# UserRegistrationAPIView
class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

# UserViewSet
class RestaurantRegistrationAPIView(generics.CreateAPIView):
    serializer_class = RestaurantRegistrationSerializer

# UserViewSet
class ReviewRegistrationAPIView(generics.CreateAPIView):
    serializer_class = ReviewRegistrationSerializer
    permission_classes = [IsAuthenticated]

# SearchRestaurantAPIView using filtersets for the search functionality
class SearchRestaurantAPIView(generics.ListAPIView):
    serializer_class = RestaurantSearchSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchRestaurantFilter

    # queryset of restaurants
    def get_queryset(self):
        return Restaurant.objects.all()
    
    # context for serializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['latitude'] = self.kwargs.get('latitude')
        context['longitude'] = self.kwargs.get('longitude')
        return context

# RestaurantsAroundUserAPIView
class RestaurantsAroundUserAPIView(APIView):

    def post(self, request):

        # get the longitude and latitude from the post
        longitude = request.data.get("longitude")
        latitude = request.data.get("latitude")

        # pass it to the google api
        google_api_functions(longitude, latitude)

        # get all restaurants
        queryset = Restaurant.objects.all()

        within_distance = {}

        # loop through using haversine forumla to see if they are within distance, in this case its 2km
        for item in queryset:
            distance = haversine((float(longitude), float(latitude)), item.get_location())
            if distance < 5:
                within_distance[item.get_id()] = {'location':item.get_location()}

        # reload hybrid recommender as new restaurants added
        model = HybridRecommender.load()
        model.update_content_recommender()

        # return the closest restaurants
        return Response(within_distance, status=status.HTTP_200_OK)
            
# RecommendRestaurantContentAPIView
class RecommendRestaurantContentAPIView(APIView):

    def get(self, request, restaurant_id, longitude, latitude):

        # load recommender and query the content recommender
        model = HybridRecommender.load()
        restaurants = model.query_content_recommender(restaurant_id)

        # loop through the id's getting the restaurant information
        response_data = []
        for item in restaurants:

            # get the restaurant info
            restaurant = Restaurant.objects.get(id=item)

            # append it tp the response data
            response_data.append({
                "id": restaurant.get_id(),
                "name": restaurant.get_name(),
                "type": restaurant.get_type(),
                "price_level": restaurant.get_price_level(),
                "average_rating": restaurant.get_average_rating(),
                "distance_from_user": haversine((float(longitude), float(latitude)), restaurant.get_location()),
                "open_or_close": get_open_or_close(restaurant)
        })
            
        # return the recommended restaurants
        return Response(response_data, status=status.HTTP_200_OK)

# RecommendRestaurantCollaborativeAPIView
class RecommendRestaurantCollaborativeAPIView(APIView):

    def get(self, request):

        # load the recommender and query the collaborative recommender
        model = HybridRecommender.load()
        restaurants = model.query_collaborative_recommender(request.user.id)

        # return the recommended restaurants
        return Response(restaurants, status=status.HTTP_200_OK)
    
# RecommendRestaurantHybridAPIView
class RecommendRestaurantHybridAPIView(APIView):

    def get(self, request, longitude, latitude):

        # load the recommender and query the hybrid recommender
        model = HybridRecommender.load()
        restaurants = model.query_hybrid_recommender(request.user.id)

        # loop through the id's getting the restaurant information
        response_data = []
        unique_list = []
        for item in restaurants:

            # hybrid could have duplicate id's so make sure nothing can be returned twice
            if item not in unique_list:
                unique_list.append(item)
                
                # get the restaurant info
                restaurant = Restaurant.objects.get(id=item)

                # append it tp the response data
                response_data.append({
                    "id": restaurant.get_id(),
                    "name": restaurant.get_name(),
                    "type": restaurant.get_type(),
                    "price_level": restaurant.get_price_level(),
                    "average_rating": restaurant.get_average_rating(),
                    "distance_from_user": haversine((float(longitude), float(latitude)), restaurant.get_location()),
                    "open_or_close": get_open_or_close(restaurant)
                })

        # return the recommended restaurants
        return Response(response_data, status=status.HTTP_200_OK)

# ReviewUserAPIView
class ReviewUserAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    # queryset of reviews
    def get_queryset(self):

        # get the user making the query and get all the reviews that they have made
        user = self.request.user
        test = Review.objects.filter(user=user)
        # return the reviews
        return test
    
# ReviewRestaurantAPIView
class ReviewRestaurantAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    # querset of reviews
    def get_queryset(self):

        # get which the reviews for a specific restaurant
        restaurant_id = self.kwargs.get('restaurant_id')
        test = Review.objects.filter(restaurant_id=restaurant_id)
        # return the reviews
        return test

class UserPasswordUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        # check old password
        if request.user.password != current_password:
            return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        
        # if no errors then set new password
        request.user.set_password(new_password)
        request.user.save()

        return Response({'detail': 'Success'}, status=status.HTTP_200_OK)
from .models import *
from .serializers import *
from .requests import *
from .formula import *

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
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SearchRestaurantFilter

    # queryset of restaurants
    def get_queryset(self):
        return Restaurant.objects.all()

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
            if distance < 2:
                within_distance[item.get_name()] = {'distance':distance, 'location':item.get_location(), 'rating':item.get_average_rating()}

        # reload hybrid recommender as new restaurants added
        model = HybridRecommender.load()
        model.update_content_recommender()

        # return the closest restaurants
        return Response(within_distance, status=status.HTTP_200_OK)
    
# RecommendRestaurantContentAPIView
class RecommendRestaurantContentAPIView(APIView):

    def get(self, request, restaurant_id):

        # load recommender and query the content recommender
        model = HybridRecommender.load()
        restaurants = model.query_content_recommender(restaurant_id)

        # return the recommended restaurants
        return Response(restaurants, status=status.HTTP_200_OK)

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

    def get(self, request):

        # load the recommender and query the hybrid recommender
        model = HybridRecommender.load()
        restaurants = model.query_hybrid_recommender(request.user.id)

        # return the recommended restaurants
        return Response(restaurants, status=status.HTTP_200_OK)

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
    permission_classes = [IsAuthenticated]

    # querset of reviews
    def get_queryset(self):

        # get which the reviews for a specific restaurant
        restaurant_id = self.kwargs.get('restaurant_id')
        test = Review.objects.filter(restaurant_id=restaurant_id)
        # return the reviews
        return test


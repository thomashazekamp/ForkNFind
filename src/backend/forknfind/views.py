from .models import *
from .serializers import *
from .requests import *
from .formula import *

from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = UserSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RestaurantCategoryViewSet(viewsets.ModelViewSet):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class RestaurantRegistrationAPIView(generics.CreateAPIView):
    serializer_class = RestaurantRegistrationSerializer

class ReviewRegistrationAPIView(generics.CreateAPIView):
    serializer_class = ReviewRegistrationSerializer
    permission_classes = [IsAuthenticated]

class RestaurantsAroundUserAPIView(APIView):

    def post(self, request):

        longitude = request.data.get("longitude")
        latitude = request.data.get("latitude")

        google_api_functions(longitude, latitude)

        queryset = Restaurant.objects.all()

        within_distance = {}

        for item in queryset:
            distance = haversine((float(longitude), float(latitude)), item.get_location())
            if distance < 2:
                within_distance[item.get_name()] = {'distance':distance, 'location':item.get_location(), 'rating':item.get_average_rating()}


        return Response(within_distance, status=status.HTTP_200_OK)
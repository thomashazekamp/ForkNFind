from .models import *
from .serializers import *

from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

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

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class RestaurantRegistrationAPIView(generics.CreateAPIView):
    serializer_class = RestaurantRegistrationSerializer

class ReviewRegistrationAPIView(generics.CreateAPIView):
    serializer_class = ReviewRegistrationSerializer
    permission_classes = [IsAuthenticated]
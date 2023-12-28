from .models import *
from .serializers import *

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

        print(request.data.get("longitude"))
        print(request.data.get("latitude"))
        return Response({'result': "result"}, status=status.HTTP_200_OK)
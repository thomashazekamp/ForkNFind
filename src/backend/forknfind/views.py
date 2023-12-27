from .models import *
from .serializers import *

from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = UserSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

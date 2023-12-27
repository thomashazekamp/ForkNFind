from .models import *
from .serializers import *

from django.shortcuts import render
from rest_framework import viewsets, generics, filters

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = UserSerializer

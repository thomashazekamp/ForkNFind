from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
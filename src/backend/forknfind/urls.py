from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'restaurant', RestaurantViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/user/', UserRegistrationAPIView.as_view(), name="api_register_user"),
    path('register/restaurant/', RestaurantRegistrationAPIView.as_view(), name="api_register_restaurant"),
    path('register/review/', ReviewRegistrationAPIView.as_view(), name="api_register_review"),
]
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'restaurant', RestaurantViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'restaurantcategory', RestaurantCategoryViewSet)
router.register(r'restauranttime', RestaurantTimeViewSet)
router.register(r'restaurantday', RestaurantDayViewSet)
router.register(r'restauranthours', RestaurantHoursViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/user/', UserRegistrationAPIView.as_view(), name="api_register_user"),
    path('register/restaurant/', RestaurantRegistrationAPIView.as_view(), name="api_register_restaurant"),
    path('register/review/', ReviewRegistrationAPIView.as_view(), name="api_register_review"),
    path('find/restaurants/', RestaurantsAroundUserAPIView.as_view(), name="api_find_restaurants"),
    path('search/restaurant/', SearchRestaurantAPIView.as_view() ,name="api_search_restaurants"),
    path('recommend/content/<int:restaurant_id>/', RecommendRestaurantContentAPIView.as_view(), name="api_recommend_restaurant_content"),
    path('recommend/collaborative/', RecommendRestaurantCollaborativeAPIView.as_view(), name="api_recommend_restaurant_collaborative"),
    path('recommend/hybrid/', RecommendRestaurantHybridAPIView.as_view(), name="api_recommend_restaurant_hybrid"),
]
from django.urls import path, include
from .views import *
from rest_framework import routers

# default routers for class instances
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
    path('api/', include(router.urls)), # for the default routers
    path('register/user/', UserRegistrationAPIView.as_view(), name="api_register_user"), # API to register a user
    path('register/restaurant/', RestaurantRegistrationAPIView.as_view(), name="api_register_restaurant"), # API to register a restaurant
    path('register/review/', ReviewRegistrationAPIView.as_view(), name="api_register_review"), # API to register a review
    path('find/restaurants/', RestaurantsAroundUserAPIView.as_view(), name="api_find_restaurants"), # API to find restaurants around user
    path('search/restaurant/<latitude>/<longitude>/', SearchRestaurantAPIView.as_view() ,name="api_search_restaurants"), # API to search restaurants 
    path('recommend/content/<int:restaurant_id>/', RecommendRestaurantContentAPIView.as_view(), name="api_recommend_restaurant_content"), # API to query content recommender
    path('recommend/collaborative/', RecommendRestaurantCollaborativeAPIView.as_view(), name="api_recommend_restaurant_collaborative"), # API to query collaborative recommender
    path('recommend/hybrid/', RecommendRestaurantHybridAPIView.as_view(), name="api_recommend_restaurant_hybrid"), # API to query hybrid recommender
    path('review/user/', ReviewUserAPIView.as_view(), name="api_user_reviews"), # API to see all user reviews
    path('review/restaurant/<int:restaurant_id>/', ReviewRestaurantAPIView.as_view(), name="api_restaurant_reviews"), # API to see all restaurant reviews
]
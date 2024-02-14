from .models import *
import random

# Sample reviews
review_options = {1:[1,"I hate this Restaurant"],
                  2:[2,"I was not a fan of this Restaurant"],
                  3:[3,"This restaurant was okay"],
                  4:[4,"The food in this restaurant was okay"],
                  5:[5,"The restaurant had both excellent service and a great set of staff"]}


def reviewCreator():

    # Get all restaurants and loop through each one
    all_restaurants = Restaurant.objects.all()
    for restaurant in all_restaurants:

        # Get the number of reviews for each restaurant
        restaurant_reviews = Review.objects.filter(restaurant=restaurant)
        number_of_reviews = len(restaurant_reviews)

        # While the number of reviews is less than 10
        while number_of_reviews < 10:

            # Randomly create user reviews with random users to increase the amount
            random_user = APIUser.objects.order_by('?').first()
            review_content = review_options[random.randint(1,5)]

            new_review = Review.objects.create( user=random_user,
                                                restaurant=restaurant,
                                                rating=review_content[0],
                                                description=review_content[1])
            new_review.save()

            number_of_reviews += 1

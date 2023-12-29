import math

# Haversine formula for calculating the distance between two locations, using longitude and latitude 
def haversine(user_location, restaurant_location):
    
    # Set up
    user_longitude, user_latitude, restaurant_longitude, restaurant_latitude = map(math.radians, [user_location[0], user_location[1], restaurant_location[0], restaurant_location[1]])

    difference_latitude = restaurant_latitude - user_latitude
    difference_longitude = restaurant_longitude - user_longitude

    radius_of_earth = 6371 # Kilometers

    # Haversine formula
    a = math.sin(difference_latitude/2)**2 + math.cos(user_latitude) * math.cos(restaurant_latitude) * math.sin(difference_longitude/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = radius_of_earth * c

    return distance
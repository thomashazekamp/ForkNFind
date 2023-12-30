import requests
from .models import *

def google_maps_nearby_search(longitude, latitude):

    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": "REDACTED_GOOGLE_MAPS_API_KEY",
        "X-Goog-FieldMask": "places.displayName,places.id",
    }

    data = {
        "includedTypes": ["restaurant"],
        "maxResultCount": 5,
        "rankPreference": "DISTANCE",
        "locationRestriction": {
            "circle": {
                "center": {"latitude": longitude, "longitude": latitude},
                "radius": 1000.0,
            }
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:

        restaurant_info = response.json()
        return restaurant_info
    
    else:
        print(f"I have no idea what is the issue in this case: {response.status_code} -- {response.text}")

def google_maps_individual_search(id):

    url = "https://places.googleapis.com/v1/places/" + id

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": "REDACTED_GOOGLE_MAPS_API_KEY",
        "X-Goog-FieldMask": "name,location,displayName,types,priceLevel,allowsDogs,delivery,dineIn,goodForChildren,goodForGroups,outdoorSeating,parkingOptions,primaryType,formattedAddress,primaryType,primaryTypeDisplayName,paymentOptions,reservable",
    }

    #print(url)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        restaurant_info = response.json()

        add_restaurant_to_database(id, restaurant_info)

        return restaurant_info
    
    else:
        print(f"I have no idea what is the issue in this case: {response.status_code} -- {response.text}")

def individual_restaurant_information(id):

    try:
        instance = Restaurant.objects.get(google_id=id)
        print(instance)

    except Restaurant.DoesNotExist:

        # When restaurant is not in the database
        google_maps_individual_search(id)

def add_restaurant_to_database(id, restaurant_info):

    google_id = id
    longitude, latitude, name, type, price_level, allows_dogs, delivery, dine_in, good_for_children, good_for_groups, outdoor_seating, address = extract_restaurant_info(restaurant_info)

    new_restaurant = Restaurant.objects.create(google_id=google_id, longitude=longitude, latitude=latitude, name=name, type=type, price_level=price_level, allows_dogs=allows_dogs, delivery=delivery, dine_in=dine_in, good_for_children=good_for_children, good_for_groups=good_for_groups, outdoor_seating=outdoor_seating, address=address, average_rating=0)
    new_restaurant.save()

    categories = restaurant_info['types']

    for category in categories:

        try:
            instance = Category.objects.get(category=category)

            new_restaurant_category = RestaurantCategory.objects.create(restaurant=new_restaurant, category=instance)
            new_restaurant_category.save()

        except Category.DoesNotExist:

            new_category = Category.objects.create(category=category)
            new_category.save()

            new_restaurant_category = RestaurantCategory.objects.create(restaurant=new_restaurant, category=new_category)
            new_restaurant_category.save()

def extract_restaurant_info(restaurant_info):

    longitude = restaurant_info['location']['latitude']
    latitude = restaurant_info['location']['longitude']
    name = restaurant_info['displayName']['text']

    try:
        type = restaurant_info['primaryType']
    except KeyError:
        type = "unknown"
    try:
        address = restaurant_info['formattedAddress']
    except:
        address = "unknown"
    try:
        price_level = restaurant_info['priceLevel']
    except KeyError:
        price_level = 'PRICE_LEVEL_INEXPENSIVE'
    try:
        allows_dogs = restaurant_info['allowsDogs']
    except KeyError:
        allows_dogs = False
    try:
        delivery = restaurant_info['delivery']
    except KeyError:
        delivery = False
    try:
        dine_in = restaurant_info['dineIn']
    except KeyError:
        dine_in = False
    try:
        good_for_children = restaurant_info['goodForChildren']
    except KeyError:
        good_for_children = False
    try:
        good_for_groups = restaurant_info['goodForGroups']
    except KeyError:
        good_for_groups = False
    try:
        outdoor_seating = restaurant_info['outdoorSeating']
    except KeyError:
        outdoor_seating = False

    return longitude, latitude, name, type, price_level, allows_dogs, delivery, dine_in, good_for_children, good_for_groups, outdoor_seating, address

def google_api_functions(longitude, latitude):
    
    collected_restaurants = google_maps_nearby_search(longitude, latitude)

    #print(collected_restaurants)

    for item in collected_restaurants['places']:

        individual_restaurant_information(item['id'])
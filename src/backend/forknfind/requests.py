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
        "X-Goog-FieldMask": "name,location",
    }

    print(url)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        restaurant_info = response.json()
        
        print(restaurant_info)

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

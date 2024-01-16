import requests
from .models import *

# searching google maps nearby to return restaurants
def google_maps_nearby_search(longitude, latitude):

    # url to search
    url = "https://places.googleapis.com/v1/places:searchNearby"

    # headers to include
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": "REDACTED_GOOGLE_MAPS_API_KEY",
        "X-Goog-FieldMask": "places.displayName,places.id",
    }

    # data to send, has to be a restaurant, ranked via distance and longitude and latitude coordinates passed in
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

    # sent the request with the information
    response = requests.post(url, json=data, headers=headers)

    # if it worked then get the json and return it
    if response.status_code == 200:

        restaurant_info = response.json()
        return restaurant_info
    # if it broke then it has not been seen yet what it sent as we haven't broke it
    else:
        print(f"I have no idea what is the issue in this case: {response.status_code} -- {response.text}")

# searching google maps for a specific restaurants details
def google_maps_individual_search(id):

    # url to search
    url = "https://places.googleapis.com/v1/places/" + id

    # headers to include
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": "REDACTED_GOOGLE_MAPS_API_KEY",
        "X-Goog-FieldMask": "name,location,displayName,types,priceLevel,allowsDogs,delivery,dineIn,goodForChildren,goodForGroups,outdoorSeating,parkingOptions,primaryType,formattedAddress,primaryType,primaryTypeDisplayName,paymentOptions,reservable,regularOpeningHours",
    }

    # sent the request with the information
    response = requests.get(url, headers=headers)

    # if it worked then get the json and add the information to the database
    if response.status_code == 200:

        restaurant_info = response.json()

        add_restaurant_to_database(id, restaurant_info)

        return restaurant_info
    
    # if it broke then it has not been seen yet what it sent as we haven't broke it
    else:
        print(f"I have no idea what is the issue in this case: {response.status_code} -- {response.text}")

# check to see if we have detailed information on a restaurant using google_id
def individual_restaurant_information(id):

    # if we do have information then its okay, if not then call the google api to get the information
    try:
        instance = Restaurant.objects.get(google_id=id)
        print(instance)

    except Restaurant.DoesNotExist:

        # When restaurant is not in the database
        google_maps_individual_search(id)

# check to see if the current time exists that the restaurant opens or closes at
def check_open_and_close_time(time, point):

    # if it does then get the instance, if not create a new instance for it
    try:
        instance = RestaurantTime.objects.get(hour=time[point]['hour'], minute=time[point]['minute'])

    except RestaurantTime.DoesNotExist:
        instance = RestaurantTime.objects.create(hour=time[point]['hour'], minute=time[point]['minute'])
    # return the instance
    return instance
    
# check to see if the current day exists that the restaurant opens or closes at
def check_restaurant_day(open, close):

    # if it does then get the instance, if not create a new instance for it
    try:
        instance = RestaurantDay.objects.get(open=True, open_time=open, close_time=close)

    except RestaurantDay.DoesNotExist:
        instance = RestaurantDay.objects.create(open=True, open_time=open, close_time=close)
    # return the instance
    return instance

# adding the restaurant information to the database
def add_restaurant_to_database(id, restaurant_info):

    # get the information about the restaurant
    google_id = id
    longitude, latitude, name, type, price_level, allows_dogs, delivery, dine_in, good_for_children, good_for_groups, outdoor_seating, address = extract_restaurant_info(restaurant_info)

    # create a new instance for the restaurant
    new_restaurant = Restaurant.objects.create(google_id=google_id, longitude=longitude, latitude=latitude, name=name, type=type, price_level=price_level, allows_dogs=allows_dogs, delivery=delivery, dine_in=dine_in, good_for_children=good_for_children, good_for_groups=good_for_groups, outdoor_seating=outdoor_seating, address=address, average_rating=0)

    # get the opening times for the restaurant    
    open_times = restaurant_info['regularOpeningHours']['periods']

    # get the tmp_time which is when the restaurant doesn't open that day
    tmp_time = RestaurantDay.objects.get(open=False, open_time=None, close_time=None)

    new_times = { 
        'monday': tmp_time,
        'tuesday': tmp_time,
        'wednesday': tmp_time,
        'thursday': tmp_time,
        'friday': tmp_time,
        'saturday': tmp_time,
        'sunday': tmp_time
    }

    # loop through the data to add the real times the restaurant opens and closes at
    for time in open_times:

        # for each check if the instances already exist of both the times and the days
        if time['open']['day'] == 0:
            new_times['monday'] = check_restaurant_day(check_open_and_close_time(time, 'open'), check_open_and_close_time(time, 'close'))
        elif time['open']['day'] == 1:
            new_times['tuesday'] = check_restaurant_day(check_open_and_close_time(time, 'open'), check_open_and_close_time(time, 'close'))
        elif time['open']['day'] == 2:
            new_times['wednesday'] = check_restaurant_day(check_open_and_close_time(time, 'open'), check_open_and_close_time(time, 'close'))
        elif time['open']['day'] == 3:
            new_times['thursday'] = check_restaurant_day(check_open_and_close_time(time, 'open'), check_open_and_close_time(time, 'close'))
        elif time['open']['day'] == 4:
            new_times['friday'] = check_restaurant_day(check_open_and_close_time(time, 'open'), check_open_and_close_time(time, 'close'))
        elif time['open']['day'] == 5:
            new_times['saturday'] = check_restaurant_day(check_open_and_close_time(time, 'open'), check_open_and_close_time(time, 'close'))
        elif time['open']['day'] == 6:
            new_times['sunday'] = check_restaurant_day(check_open_and_close_time(time, 'open'), check_open_and_close_time(time, 'close'))

    # see if a instance of the week already exists, if not create one
    try:
        restaurant_hours = RestaurantHours.objects.get(monday=new_times['monday'], tuesday=new_times['tuesday'], wednesday=new_times['wednesday'], thursday=new_times['thursday'], friday=new_times['friday'], saturday=new_times['saturday'], sunday=new_times['sunday'])
    
    except RestaurantHours.DoesNotExist:
        restaurant_hours = RestaurantHours.objects.create(monday=new_times['monday'], tuesday=new_times['tuesday'], wednesday=new_times['wednesday'], thursday=new_times['thursday'], friday=new_times['friday'], saturday=new_times['saturday'], sunday=new_times['sunday'])
    
    # save it to the new instance of restaurant
    new_restaurant.hours = restaurant_hours

    # save the restaurant instance
    new_restaurant.save()

    # loop throught the categories associated with the restaurant
    categories = restaurant_info['types']

    for category in categories:

        # check if the category already exists and if so create a join instance between them, if it doesnt exist create a new instance for that class and create a join instance
        try:
            instance = Category.objects.get(category=category)

            new_restaurant_category = RestaurantCategory.objects.create(restaurant=new_restaurant, category=instance)
            new_restaurant_category.save()

        except Category.DoesNotExist:

            new_category = Category.objects.create(category=category)
            new_category.save()

            new_restaurant_category = RestaurantCategory.objects.create(restaurant=new_restaurant, category=new_category)
            new_restaurant_category.save()

# extracting the data from the restaurant json returned from google
def extract_restaurant_info(restaurant_info):

    longitude = restaurant_info['location']['latitude']
    latitude = restaurant_info['location']['longitude']
    name = restaurant_info['displayName']['text']

    # lots of trys and errors incase the data is not there, if it is save it, if not leave blank
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

    # return all the attributes
    return longitude, latitude, name, type, price_level, allows_dogs, delivery, dine_in, good_for_children, good_for_groups, outdoor_seating, address

# google api function for calling the other functions
def google_api_functions(longitude, latitude):
    
    # calls the nearby search
    collected_restaurants = google_maps_nearby_search(longitude, latitude)

    # for each restaurant returned check if it has an instance in the database
    for item in collected_restaurants['places']:

        individual_restaurant_information(item['id'])
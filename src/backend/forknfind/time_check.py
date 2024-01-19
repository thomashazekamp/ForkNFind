from datetime import datetime, time

# Calculates whether a resturant is open or closed
def time_check_function(restaurantday):

    # check if the restaurant opens on this day
    if restaurantday.get_open() == False:
        return "Closed"

    # get the instances of RestaurantTime
    open_time = restaurantday.get_open_time()
    close_time = restaurantday.get_close_time()

    # converts to instances of Time
    open_time = time(open_time.get_hour(), open_time.get_minute())
    close_time = time(close_time.get_hour(), close_time.get_minute())

    # the current time the request has been made
    current_time = datetime.now().time()

    # check if the current time is between the open time and close time
    if open_time <= current_time <= close_time:
        return "Open"
    else:
        return "Closed"

# Calculates whether a restaurant is currently open or closed
def get_open_or_close(obj):
        
        # work out the current day
        current_datetime = datetime.now()
        current_day = current_datetime.weekday()

        if obj.get_hours() is None:
            return "Closed"
        week_time = obj.get_hours()

        if current_day == 0:
            return time_check_function(week_time.get_monday())
        elif current_day == 1:
            return time_check_function(week_time.get_tuesday())
        elif current_day == 2:
            return time_check_function(week_time.get_wednesday())
        elif current_day == 3:
            return time_check_function(week_time.get_thursday())
        elif current_day == 4:
            return time_check_function(week_time.get_friday())
        elif current_day == 5:
            return time_check_function(week_time.get_saturday())
        elif current_day == 6:
            return time_check_function(week_time.get_sunday())
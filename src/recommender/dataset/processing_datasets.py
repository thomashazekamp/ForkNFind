import pandas as pd
import numpy as np
import csv

def business():

    csv_file_open = 'clean_dataset/business.csv'
    business_data = pd.read_csv(csv_file_open)

    csv_file_processed = 'processed_dataset/business.csv'

    # Approved business's that are both restaurants and are in the city of Philadelphia
    sorted_data = []

    # Loop through each row of the dataframe only keeping those in the city of Philadelphia and that have the category restaurant in it
    for _, row in business_data.iterrows():
        place = row['city'] # Place the business is
        category = row['categories'] # Category of the business
        if pd.isna(place) or pd.isna(category): # If either the place or category is empty then move on as we can't check if either in Philadelphia or if it is a restaurant
            pass
        elif place == 'Philadelphia' and 'Restaurants' in category: # If both in Philadelphia and a Restaurant then add to the list of approved Business
            sorted_data.append(row)



    with open(csv_file_processed, 'w', newline='', encoding='utf-8') as csv_file: # Open the file
        csv_writer = csv.writer(csv_file)

        # Write CSV header first
        csv_writer.writerow(['business_id', 'city', 'stars', 'attributes', 'categories'])
        for line in sorted_data: # Loop through the data putting in the Business information we are keeping
            csv_writer.writerow([line[0],line[1],line[2],line[3],line[4]])

    business_data = pd.read_csv(csv_file_processed) 



    # Creating new ID's for each business
    business_data['old_business_id'] = business_data['business_id']
    business_data['business_id'] = range(1, len(business_data) + 1)



    categories = {} # Store each individual category and how many times it appears in the restaurants.

    for _, row in business_data.iterrows():
        # Loop through each row in dataframe
        if not pd.isna(row['categories']): # Make sure it is not NaN
            categories_split = row['categories'].split(', ') # Split up the categories
            for category in categories_split: # Loop through each individual category per restaurant
                if category in categories: # If the category is already in the dictionary then add 1 to the value
                    categories[category] += 1 
                else: # If the category is not in the dictionary then save it to the dictionary and set the value to 1
                    categories[category] = 1



    categories.pop("Restaurants") # Pop this from the dictionary as they all have this value



    # We will take the first 40 Categories to use for restaurants as comparison
    cleaned_categories = [] # List of the categories that will be used in item to item comparison
    count = 0 # Count to keep track that we only take 40 categories

    for key, _ in categories.items(): # Loop through the dictionary
        if count == 40: # Break when count gets to 40
            break
        cleaned_categories.append(key) # List of all the categories
        count += 1

    print(cleaned_categories)

    for key in cleaned_categories: # Loop through the list of categories
        current_categories = [] # Storage for each row and whether that category appears or not
        for index, row in business_data.iterrows(): # Loop through business dataframe
            if not pd.isna(row['categories']): # Make sure the Restaurant has categories
                categories_split = row['categories'].split(', ') # Split the current categories up
                check = False # Have a check to see if the category is found
                for category in categories_split: # Convert string into dictionary
                    if category == key: # If the category is found then append 1 to a list
                        current_categories.append(1)
                        check = True
                if check == False: # If it is not found append a 0 to a list
                    current_categories.append(0)
            else: # If the category column is NaN then add a 0
                current_categories.append(0)

        business_data[key] = current_categories # Save the new column for that new category to the dataframe

    # Remove the category column from the dataframe
    business_data = business_data.drop('categories', axis=1)

    business_data.to_csv(csv_file_processed)

    # Still have to do it to Attributes for the restaurants

    review()



    business_data.drop('old_business_id', axis=1)
    business_data.to_csv(csv_file_processed)

    

    print("Business Done")

def review():

    csv_file = 'clean_dataset/review.csv'
    review_data = pd.read_csv(csv_file)
    business_data = pd.read_csv('processed_dataset/business.csv')

    unique_business_id = business_data.old_business_id.unique()
    filtered_df = review_data[review_data['business_id'].isin(unique_business_id)]



    filtered_df['date'] = pd.to_datetime(filtered_df['date'])
    filtered_df = filtered_df.sort_values(by='date').groupby(['user_id', 'business_id']).tail(1)



    id_mapping = dict(zip(business_data['old_business_id'], business_data['business_id']))
    # Replace old business IDs in 'filtered_df' with new business IDs
    filtered_df['business_id'] = filtered_df['business_id'].map(id_mapping)



    # Creating new ID's for each review
    len(filtered_df)
    filtered_df['review_id'] = range(1, len(filtered_df) + 1)



    # Creating new ID's for each user
    user_id_mapping = {user_id: idx + 1 for idx, user_id in enumerate(np.unique(filtered_df['user_id']))}
    filtered_df['user_id'] = filtered_df['user_id'].map(user_id_mapping)

    filtered_df.drop('date', axis=1)

    filtered_df.reset_index(drop=True, inplace=True)
    filtered_df.to_csv('processed_dataset/review.csv', index=False)

    print("Review Done")

def main():

    business()

main()
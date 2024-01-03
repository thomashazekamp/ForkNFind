import pandas as pd

def business():

    json_file = 'original_dataset/yelp_academic_dataset_business.json'
    df = pd.read_json(json_file, lines=True)

    columns_needed = ['business_id', 'city', 'stars', 'attributes', 'categories']
    df_processed = df[columns_needed]

    csv_file = 'clean_dataset/business.csv'
    df_processed.to_csv(csv_file, index=False)

    print("Business Done")

def review():

    # This code requires more then 32gb of RAM, so have to divide up too run
    limiter = 1000000

    json_file = 'original_dataset/yelp_academic_dataset_review.json'
    reader = pd.read_json(json_file, lines=True, chunksize=limiter)
    df_processed = pd.DataFrame(columns=['review_id', 'user_id', 'business_id', 'stars', 'date'])

    for read in reader:
        read_processed = read[['review_id', 'user_id', 'business_id', 'stars', 'date']]
        df_processed = pd.concat([df_processed, read_processed], ignore_index=True)

    csv_file = 'clean_dataset/review.csv'
    df_processed.to_csv(csv_file, index=False)

    print("Review Done")

def main():

    business()
    review()

main()
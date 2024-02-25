'''
This file is the runner file that will call all the necessary functions to run the sentiment analysis model
'''
from dataset_worker import read_dataset, apply_dataset_column_modifications

# Read dataset
df = read_dataset()

# Apply text processing and modifications to the dataset
df = apply_dataset_column_modifications(df)

def main():
    # print(df.head())
    pass

if __name__ == '__main__':
    main()

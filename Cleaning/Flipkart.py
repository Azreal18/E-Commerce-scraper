import warnings
warnings.filterwarnings('ignore')
import time 
import pandas as pd 
import sys 
import numpy as np
import os
from datetime import date

# Replace 'your_csv_directory_path' with the path to the directory containing your CSV files
csv_directory_path = 'Path to where the files are present'

# List all files in the directory
files_in_directory = os.listdir(csv_directory_path)

# Get the current date
current_date = date.today().strftime("%Y-%m-%d")

# Create a folder with the name 'Flipkart_date of the run'
folder_name = f'Flipkart_fruits'
folder_path = os.path.join(csv_directory_path, folder_name)
os.makedirs(folder_path)
df3 = pd.DataFrame(columns =['Date','Item','QTY & price','Price','Link'])

# Loop through each file and clean if the name starts with 'Flipkart_'
for file_name in files_in_directory:
    if file_name.startswith('Flipkart_') and file_name.endswith('.csv'):
        # Construct the full path of the CSV file
        csv_file_path = os.path.join(csv_directory_path, file_name)
        
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Perform the cleaning process
        df = df.drop(df[df['Item'].str.contains('not available', case=False, na=False)].index)
        df = df.drop(df[df['Price'].str.contains('not available', case=False, na=False)].index)
        df = df.drop(df[df['Link'].str.contains('not available', case=False, na=False)].index)
        df.reset_index(drop=True, inplace=True)
        df = df.drop_duplicates(subset=['Item', 'Price', 'Link'], keep='first')
        df.reset_index(drop=True, inplace=True)
        
        # Append the cleaned data to df3
        df3 = pd.concat([df3, df], ignore_index=True)

# Replace 'Combined_Flipkart_cleaned.csv' with the desired name for the new CSV file
combined_csv_file_path = os.path.join(csv_directory_path, 'Flipkart_cleaned.csv')

# Save the combined cleaned data to a new CSV file
df3.to_csv(combined_csv_file_path, index=False)

print("Cleaning and combining of CSV files completed!")
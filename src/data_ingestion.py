import boto3
import pandas as pd
import os

# Create folder if it does not exist
os.makedirs("data/raw", exist_ok=True)

print("Downloading data from S3...")
s3 = boto3.client('s3')
# Replace with your actual bucket and file name
s3.download_file('vadid-mlops', 'IMDB.csv', 'data/raw/IMDB.csv')

print("Processing data...")
# Read data
df = pd.read_csv('data/raw/IMDB.csv')

# Clean data step-by-step
df_dropped = df.dropna()
df_final = df_dropped.drop_duplicates()

# Save final data
df_final.to_csv('data/raw/data.csv', index=False)
print("Data ingestion complete.")
import pandas as pd
import os

# Define file paths
RAW_DATA_PATH = "data/raw/h1b_data_2024.csv"
PROCESSED_DATA_PATH = "data/processed/h1b_cleaned_2024.csv"

# Function to clean and process data
def process_h1b_data():
    # Load data
    df = pd.read_csv(RAW_DATA_PATH)
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # Handle missing values
    df.fillna("Unknown", inplace=True)
    
    # Convert numerical columns
    df["initial_approval"]

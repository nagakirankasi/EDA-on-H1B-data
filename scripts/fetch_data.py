import pandas as pd
import requests
import os

# Define USCIS Data URL (Example Placeholder)
USCIS_DATA_URL = "https://example.com/h1b_data_2024.csv"
OUTPUT_PATH = "data/raw/h1b_data_2024.csv"

# Function to Fetch Data
def fetch_h1b_data():
    response = requests.get(USCIS_DATA_URL)
    if response.status_code == 200:
        os.makedirs("data/raw", exist_ok=True)
        with open(OUTPUT_PATH, "wb") as file:
            file.write(response.content)
        print(f"Data successfully saved to {OUTPUT_PATH}")
    else:
        print("Failed to fetch data. Check the URL.")

if __name__ == "__main__":
    fetch_h1b_data()

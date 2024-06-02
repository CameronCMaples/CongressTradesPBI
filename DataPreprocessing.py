import pandas as pd
import numpy as np
import re

# Load the dataset
data = pd.read_excel(r'FILEPATH\Datasets\congress-trading-all (1).xlsx')

# Data cleaning
# Convert 'Traded' and 'Filed' columns to datetime
data['Traded'] = pd.to_datetime(data['Traded'], errors='coerce')
data['Filed'] = pd.to_datetime(data['Filed'], errors='coerce')

# I am implementing a new column to display the midpoint of the trade size ranges
def range_to_midpoint(range_str):
    if pd.isna(range_str):
        return np.nan
    # Remove non-numeric characters except dot and hyphen
    range_str = re.sub(r'[^\d.-]', '', range_str)
    parts = range_str.split('-')
    if len(parts) == 2:
        low, high = parts
        try:
            return (float(low) + float(high)) / 2
        except ValueError:
            return np.nan
    try:
        return float(range_str)
    except ValueError:
        return np.nan

# Apply the conversion function to 'Trade_Size_USD'
data['Trade_Size_Midpoint'] = data['Trade_Size_USD'].apply(lambda x: range_to_midpoint(str(x)))

# Handling missing values in all columns by filling them with 'NA', excluding Int or DT columns
columns_to_fill_na = [col for col in data.columns if col not in ['excess_return', 'last_modified', 'Traded', 'Filed']]
data.fillna({col: 'NA' for col in columns_to_fill_na}, inplace=True)
data['excess_return'].fillna(0, inplace=True)

# Forward fill or backward fill missing values in the 'last_modified' column. Can't have NA in a datetime column
data['last_modified'].fillna(method='ffill', inplace=True)


# Save cleaned data to a CSV file
cleaned_file_path = r'FILEPATH\processed_congress_trading.csv'
data.to_csv(cleaned_file_path, index=False)


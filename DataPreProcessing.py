import pandas as pd
import numpy as np
import re

# Load the dataset from QuiverQuantitative
file_path = r'C:\Users\15018\Desktop\QuiverPBI\congress-trading-all (1).xlsx'
data = pd.read_excel(file_path)

# Data cleaning
# Convert 'Traded' and 'Filed' columns to datetime
data['Traded'] = pd.to_datetime(data['Traded'], errors='coerce')
data['Filed'] = pd.to_datetime(data['Filed'], errors='coerce')

# The Trade_Size_USD column contains ranges (e.g., '1001 - 15000'), so I am displaying the median
def range_to_midpoint(range_str):
    if pd.isna(range_str):
        return np.nan
    range_str = re.sub(r'[^\d.-]', '', range_str)  # Remove non-numeric characters except dot and hyphen
    if ' - ' in range_str:
        low, high = range_str.split(' - ')
        try:
            return (float(low) + float(high)) / 2
        except ValueError:
            return np.nan
    try:
        return float(range_str)
    except ValueError:
        return np.nan
    
# Apply the conversion function to 'Trade_Size_USD'
data['Trade_Size_USD'] = data['Trade_Size_USD'].apply(range_to_midpoint)

# Filling in missing values with a descriptor
data.fillna({'Subholding': 'Unknown', 'Description': 'No Description', 'Comments': 'No Comments'}, inplace=True)

# Save cleaned data to a CSV file
cleaned_file_path = r'C:\Users\15018\Desktop\QuiverPBI\cleaned_congress_trading.csv'
data.to_csv(cleaned_file_path, index=False)

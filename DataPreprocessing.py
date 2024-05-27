import pandas as pd
import numpy as np
import re

# Load the dataset
data = pd.read_excel(r'C:\Users\15018\Desktop\QuiverPBI\Datasets\congress-trading-all (1).xlsx')

# Data cleaning
# Convert 'Traded' and 'Filed' columns to datetime
data['Traded'] = pd.to_datetime(data['Traded'], errors='coerce')
data['Filed'] = pd.to_datetime(data['Filed'], errors='coerce')

# Function to convert range strings to their midpoint
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

# Handling missing values in all columns by filling them with 'NA'
data = data.fillna('NA')

# Save cleaned data to a CSV file
cleaned_file_path = r'C:\Users\15018\Desktop\QuiverPBI\cleaned_congress_trading2.csv'
data.to_csv(cleaned_file_path, index=False)

# Display the cleaned data for verification
print(data.head())

# Check if any 'Trade_Size_Midpoint' values are still NaN
print("Rows with NaN in Trade_Size_Midpoint:", data[data['Trade_Size_Midpoint'].isna()])

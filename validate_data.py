# 1. Import the pandas library so we can use it
import pandas as pd

# 2. Tell Python where our raw CSV file is
# We use 'r' before the string to tell Python it's a raw file path (prevents errors with backslashes)
file_path = r'raw_data\olist_orders_dataset.csv'

# 3. Read the CSV file into a Pandas DataFrame (think of a DataFrame as an Excel table in memory)
print("Reading the orders data...")
df = pd.read_csv(file_path)

# 4. Show the first 5 rows of the data to see what it looks like
print("\n--- First 5 rows of the data ---")
print(df.head())

# 5. Check for missing (null) values in each column
print("\n--- Checking for missing values ---")
missing_values = df.isnull().sum()
print(missing_values)

# 6. Show the total number of rows and columns
print(f"\nTotal rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

# 7. Save a "validated" copy to a new folder (Simulating the next step in our pipeline)
# First, we create the folder if it doesn't exist
import os
if not os.path.exists('validated_data'):
    os.makedirs('validated_data')

# Save the dataframe as a new CSV
df.to_csv('validated_data/validated_orders.csv', index=False)
print("\nSuccessfully saved validated data to 'validated_data' folder!")
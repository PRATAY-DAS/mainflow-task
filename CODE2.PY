import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Handling missing values: Fill missing values with a placeholder (e.g., 0 for age)
df_filled = df.fillna({'Age': 0})

# Display the DataFrame after filling missing values
print("\nDataFrame after filling missing values:")
print(df_filled)

# Removing duplicates
df_no_duplicates = df.drop_duplicates()

# Display the DataFrame after removing duplicates
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)

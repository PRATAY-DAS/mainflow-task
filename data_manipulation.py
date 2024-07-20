import pandas as pd

# Reading the CSV file
df = pd.read_csv('yourfile.csv')

# Displaying the first few rows
print("Original DataFrame:")
print(df.head())

# Handling missing values
# Dropping rows with missing values
df_cleaned = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_cleaned.head())

# Filling missing values with a specific value (example: filling with 0)
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled.head())

# Removing duplicate rows
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicate rows:")
print(df_no_duplicates.head())

# Filtering rows where a column's value is greater than a specific value (example: 200)
filtered_df = df[df['column_name'] > 200]
print("\nFiltered DataFrame where column_name > 200:")
print(filtered_df.head())

# Sorting the DataFrame by a column (example: 'column_name')
sorted_df = df.sort_values(by='column_name')
print("\nDataFrame sorted by column_name in ascending order:")
print(sorted_df.head())

# Sorting the DataFrame by a column in descending order
sorted_df_desc = df.sort_values(by='column_name', ascending=False)
print("\nDataFrame sorted by column_name in descending order:")
print(sorted_df_desc.head())

# Grouping by a column (example: 'group_column') and calculating the mean of another column (example: 'value_column')
grouped_df = df.groupby('group_column')['value_column'].mean()
print("\nGrouped DataFrame with mean values of value_column:")
print(grouped_df.head())

# Grouping by a column and counting the occurrences
count_df = df.groupby('group_column').size()
print("\nGrouped DataFrame with count of occurrences in group_column:")
print(count_df.head())

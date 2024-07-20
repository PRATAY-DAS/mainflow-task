import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [30, 25, 28, 40, 35, 30],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Save the DataFrame to 'main.csv'
df.to_csv('main.csv', index=False)
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('main.csv')

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Filtering: Select rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]

# Display the filtered DataFrame
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Sorting: Sort the DataFrame by the 'Age' column in ascending order
sorted_df = df.sort_values(by='Age')

# Display the sorted DataFrame
print("\nSorted DataFrame by Age:")
print(sorted_df)

# Grouping: Group by 'City' and calculate the average Age in each city
grouped_df = df.groupby('City').mean()

# Display the grouped DataFrame
print("\nGrouped DataFrame by City (average age):")
print(grouped_df)

import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [30, 25, 28, 40, 35, 30],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Save the DataFrame to 'sample_data.csv'
df.to_csv('sample_data.csv', index=False)

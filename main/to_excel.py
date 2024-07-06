import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

# Create DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel
df.to_excel('output.xlsx', index=False)

print("Data written to 'output.xlsx' successfully!")
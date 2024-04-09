import csv
import random

# Define the number of columns and rows
num_columns = 32
num_rows = 540  # You can adjust this as per your requirement

# Generate random data for each column
data = []
for _ in range(num_rows):
    row = [random.choice(['DOMINANCE', 'INFLUENTIAL', 'STEADINESS', 'CONSCIENTIOUSNESS']) for _ in range(num_columns)]
    data.append(row)

# Write the data to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Q{}'.format(i) for i in range(1, num_columns + 1)])  # Write column headers
    writer.writerows(data)  # Write data rows

print("Data has been saved to 'data.csv'.")

import csv

# Function to count occurrences of each letter in a row and return the most frequent letter
def count_and_get_max(row):
    counts = {'DOMINANCE': 0, 'INFLUENTIAL': 0, 'STEADINESS': 0, 'CONSCIENTIOUSNESS': 0}
    for letter in row:
        counts[letter] += 1
    max_letter = max(counts, key=counts.get)
    return max_letter

# Read data from CSV file
with open('data.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Skip the first row (column headers) and add new column with results
for row in data[1:]:
    max_letter = count_and_get_max(row)
    row.append(max_letter)

# Write data with new column to CSV file
with open('data_with_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Results have been added to 'data_with_result.csv'.")

import csv
import random

def duplicate_data(input_file, output_file, duplicate_factor):
    # Read data from CSV file
    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        # Read header
        header = next(reader)
        # Read remaining rows
        data = list(reader)

    # Determine the number of rows to duplicate
    num_rows_to_duplicate = int(len(data) * 0.3)

    # Randomly select rows to duplicate
    rows_to_duplicate = random.sample(data, num_rows_to_duplicate)

    # Duplicate selected rows by the given factor
    duplicated_rows = []
    for row in rows_to_duplicate:
        for _ in range(duplicate_factor):
            duplicated_rows.append(row)

    # Combine original data with duplicated rows
    duplicated_data = data + duplicated_rows

    # Write updated data to a new CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(header)
        # Write duplicated data
        writer.writerows(duplicated_data)

    print(f"{num_rows_to_duplicate} rows duplicated by a factor of {duplicate_factor} and written to {output_file}")

def main():
    input_file = 'data_with_result.csv'
    output_file = 'duplicated_data.csv'
    duplicate_factor = 11  # Duplicate each selected row 5 times

    duplicate_data(input_file, output_file, duplicate_factor)

if __name__ == "__main__":
    main()

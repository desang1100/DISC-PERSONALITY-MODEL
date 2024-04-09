from collections import Counter

def find_duplicates(data):
    # Split the data into individual rows and remove the header
    rows = data.split('\n')[1:]
    
    # Create a Counter object to count occurrences of each row
    row_counts = Counter(rows)
    
    # Find duplicates (rows that occur more than once)
    duplicates = {row: count for row, count in row_counts.items() if count > 1}
    
    return duplicates

def main():
    data = """Your data goes here"""
    
    duplicates = find_duplicates(data)
    
    if duplicates:
        print("Duplicate combinations found:")
        for row, count in duplicates.items():
            print(f"Combination: {row}, Count: {count}")
    else:
        print("No duplicate combinations found.")

if __name__ == "__main__":
    main()

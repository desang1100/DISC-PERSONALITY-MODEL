# Function to calculate percentage
def calculate_percentage(category_count, total_questions):
    return (category_count / total_questions) * 100

# Input the counts of answers in each category
dominance_count = int(input("Enter the count of answers in the DOMINANCE category: "))
influential_count = int(input("Enter the count of answers in the INFLUENTIAL category: "))
conscientiousness_count = int(input("Enter the count of answers in the CONSCIENTIOUSNESS category: "))
steadiness_count = int(input("Enter the count of answers in the STEADINESS category: "))

# Total number of questions
total_questions = 32

# Calculate percentages
dominance_percentage = calculate_percentage(dominance_count, total_questions)
influential_percentage = calculate_percentage(influential_count, total_questions)
conscientiousness_percentage = calculate_percentage(conscientiousness_count, total_questions)
steadiness_percentage = calculate_percentage(steadiness_count, total_questions)

# Print the results
print("Percentage of DOMINANCE:", dominance_percentage)
print("Percentage of INFLUENTIAL:", influential_percentage)
print("Percentage of CONSCIENTIOUSNESS:", conscientiousness_percentage)
print("Percentage of STEADINESS:", steadiness_percentage)

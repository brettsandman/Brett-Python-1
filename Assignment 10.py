'''
Assignment 10
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age.
'''
# Function to get a positive integer from user input
def get_positive_integer(prompt):
    while True:
        try:
            # Ask for user input
            age = int(input(prompt))
            # Check if input is a positive number
            if age > 0:
                return age
            else:
                print("Age must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to classify age into categories
def classify_age(age):
    # Categorize based on age range
    if age < 18:
        return "Minor"
    elif age <= 65:
        return "Adult"
    else:
        return "Senior citizen"

# Main program execution starts here

# Step 1: Prompt user for age and validate input
age = get_positive_integer("Enter your age: ")

# Step 2: Classify age into a category
category = classify_age(age)

# Step 3: Display the result
print(f"You are classified as: {category}")

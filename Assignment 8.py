'''Assignment 8
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
'''
# Function to get a valid mark between 0 and 100
def get_valid_mark(subject):
    while True:
        try:
            # Ask for the user's input
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            # Check if mark is within valid range
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid input. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to calculate grade based on average
def calculate_grade(average):
    # Determine the grade based on grading scale
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Main program execution starts here

# Step 1: Get marks for three subjects with validation
mark1 = get_valid_mark("Subject 1")
mark2 = get_valid_mark("Subject 2")
mark3 = get_valid_mark("Subject 3")

# Step 2: Calculate the average of the marks
average = (mark1 + mark2 + mark3) / 3

# Step 3: Determine the grade based on the average
grade = calculate_grade(average)

# Step 4: Display the result
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")

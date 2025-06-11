'''
Assignment 12
Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.
=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.
'''
# Step 1: Prompt the user for the number of rows
while True:
    try:
        rows = int(input("Enter the number of rows for the triangle pattern: "))
        if rows > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Step 2: Prompt the user for the character to use
pattern_char = input("Enter the character to use in the pattern: ")

# Step 3: Generate the right triangle pattern using nested loops
print("Triangle Pattern:")
for i in range(1, rows + 1):
    for j in range(i):
        print(pattern_char, end="")
    print()  # Move to the next line after each row

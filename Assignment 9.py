'''
Assignment 9
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.
=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''
# Function to check if a character is a vowel
def is_vowel(char):
    return char.lower() in 'aeiou'

# Function to ensure the user enters a single alphabetical character
def get_single_letter():
    while True:
        # Ask for user input
        char = input("Enter a single letter: ")
        # Check for single character and if it's a letter
        if len(char) != 1:
            print("Error: Please enter exactly one character.")
        elif not char.isalpha():
            print("Error: Please enter a letter (A-Z or a-z).")
        else:
            return char

# Main program execution starts here

# Step 1: Get a valid single letter input
char = get_single_letter()

# Step 2: Determine whether the letter is a vowel or consonant
if is_vowel(char):
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

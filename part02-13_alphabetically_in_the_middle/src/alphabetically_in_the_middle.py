# Write your solution here

# Get inputs from the user
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# Determine the middle letter using conditional statements
if (letter1 > letter2 and letter1 < letter3) or (letter1 < letter2 and letter1 > letter3):
    middle_letter = letter1
elif (letter2 > letter1 and letter2 < letter3) or (letter2 < letter1 and letter2 > letter3):
    middle_letter = letter2
else:
    middle_letter = letter3

# Print the result
print("The letter in the middle is", middle_letter)

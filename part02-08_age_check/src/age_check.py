# Ask for the user's age
age = int(input("What is your age? "))

# Check if the age is plausible
if age < 0:
    print("That must be a mistake")
elif age < 5:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")

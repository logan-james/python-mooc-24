# Write your solution here

# Program to separate integer and decimal part of a floating point number

# Asking the user to input a floating point number
number = float(input("Please type in a number: "))

# Separating the integer part
integer_part = int(number)

# Calculating the decimal part
decimal_part = number - integer_part

# Printing the integer and decimal part
print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part}")



# Write your solution here

# Initialize variables to keep track of count, sum, positives, and negatives
count = 0 # To count the number of non-zero numbers
total_sum = 0 # To calculate the sum of non-zero numbers
positive_count = 0 # To count positive numbers
negative_count = 0 # To count negative numbers

# Prompt the user for numbers until they enter 0
print("Please type in integer numbers. Type in 0 to finish.")

while True:
  # Get input from the user and convert it to an integer
  number = int(input("Number: "))

# Check if the user entered 0 to exit the loop
  if number == 0:
    break

# Since the number is not 0, increment the count
  count += 1

# Add the number to the total sum
  total_sum += number

# Check if the number is positive or negative
  if number > 0:
    positive_count += 1
  elif number < 0:
    negative_count += 1

# After the loop ends, print the results
# Part 1: Print the count of numbers typed (excluding 0)
print(f"Number typed in {count}")

# Part 2: Print the sum of the numbers (excluding 0)
print(f"The sum of the numbers is {total_sum}")

# Part 3: Calculate and print the mean (sum / count)
# The problem states we can assume at least one non-zero number, so count won't be 0
mean = total_sum / count
print(f"The mean of the numbers is {mean}")

# Part 4: Print the count of positive and negative numbers
print(f"Positive numbers {positive_count}")
print(f"Negative numbers {negative_count}")
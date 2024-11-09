# Write your solution here
#if number div by 3 = fizz
#if num div by 5 = buzz
#if num div by both 3 AND 5 = fizzbuzz

num = int(input("Number: "))

if num % 3 == 0 and num % 5 == 0:
    # This condition must be evaluated first, because if this is true,
    # also both of the following conditions are true
  print("FizzBuzz")
elif num % 3 == 0:
  print("Fizz")
elif num % 5 == 0:
  print("Buzz")


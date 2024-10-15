# Write your solution here
a = int(input("Number 1: "))
b = int(input("Number 2: "))
operation = input("Operation: ")
if operation == "add":
  print(f" {a} + {b} = {a+b}")

if operation == "multiply":
  print(f"{a} * {b} = {a*b}")

if operation == "subtract":
  print(f"{a} - {b} = {a-b}")
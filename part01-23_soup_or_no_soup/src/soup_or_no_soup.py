# Write your solution here
name = input("Please tell me your name: ")
if name == "Jerry":
  print("Next please!")
else:
  portions = int(input("How many portions of soup? "))
  total = portions * 5.9
  print(f"The total cost is {total}")
  print("Next please!")
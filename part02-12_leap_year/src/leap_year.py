# Write your solution here

#any year div by 4 = leap year
#but if the year is also div by 100 it is leap year only
#if also div by 400 

year = int(input("Please type in a year: "))

if year % 4 == 0:
  if year % 100 == 0 and year % 400 == 0:
    print("That year is a leap year.")
  elif year % 100 == 0 and year % 400 != 0:
    print("That year is not a leap year.")
  else:
    print("That year is a leap year.")
else: 
  print("That year is not a leap year.")

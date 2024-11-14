# Write your solution here

 
value_of_gift = int(input("Value of gift: "))
if value_of_gift < 5000:
  print("No tax!")
elif value_of_gift < 25000:
  tax_amount = (100 + (value_of_gift - 5000) * .08)
  print(f"Amount of tax: {tax_amount} euros")
elif value_of_gift < 55000:
  tax_amount = (1700 + (value_of_gift - 25000) * .10)
  print(f"Amount of tax: {tax_amount} euros")
elif value_of_gift < 200000:
  tax_amount = (4700 + (value_of_gift - 55000) * .12)
  print(f"Amount of tax: {tax_amount} euros")
elif value_of_gift < 1000000:
  tax_amount = (22100 + (value_of_gift - 200000) * .15)
  print(f"Amount of tax: {tax_amount} euros")
elif value_of_gift > 1000000:
  tax_amount = (142100 + (value_of_gift - 1000000) * .17)
  print(f"Amount of tax: {tax_amount} euros")


# Write your solution here
wk = int(input("How many times a week do you eat at the student cafeteria? "))
p = float(input("The price of a typical student lunch? "))
pg = float(input("How much money do you spend on groceries in a week? "))

aw = (wk * p) + pg
ad = ((wk * p) + pg) / 7

print()
print("Average food expenditure: ")
print(f"Daily: {ad} euros")
print(f"Weekly: {aw} euros")


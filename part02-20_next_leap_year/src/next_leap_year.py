# Write your solution here


start_year = int(input("Year: "))
year = start_year + 1 #program starts checking for leap years starting after input
while True: # loop continuously until leap year breaks out
    if year % 100 == 0: #if year is div by 100 it must also be div by 400 to be leap yr
        if year % 400 == 0:
            break
    elif year % 4 == 0: #if yr is div by 4 but not 100 it is leap
        break
    year += 1

print(f"The next leap year after {start_year} is {year}")
# Write your solution here

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_next_leap_year(year):
    while True:
        year += 1
        if is_leap_year(year):
            return year

year = int(input("Year: "))
print(f"The next leap year after {year} is {get_next_leap_year(year)}")

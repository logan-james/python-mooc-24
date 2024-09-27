# working
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print("")
print(f"my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print("")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# value of using fstrings:
# print(f"Hi {name}, you are {age} years old. You live in {city}.")
# is the same as using comas, but using commas is harder syntax.
# print("Hi", name, ", you are", age, "years old. You live in", city, ".")

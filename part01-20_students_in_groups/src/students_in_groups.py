# Write your solution here

# Ask the user for the number of students and the desired group size
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

# Calculate the number of groups
num_groups = students // group_size

# If there's a remainder, add one more group for the remaining students
if students % group_size != 0:
    num_groups += 1

# Print the number of groups formed
print(f"Number of groups formed: {num_groups}")

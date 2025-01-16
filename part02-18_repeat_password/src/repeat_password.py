# Write your solution here
# while True:  
#   pw = input("Password: ")
#   repeat_pw = input("Repeat Password: ")
#   if pw == repeat_pw:
#     print("User account created!")
#     break
#   else:
#     print("They do not match!")

# Write your solution here
password = input("Password: ")
while True:
    repeat_password = input("Repeat password: ")
    if repeat_password == password:
        print("User account created!")
        break
    else:
        print("They do not match!")


print("test")
# Exercise 1 - Validate User Input
# Rules:
#   1. username is no more than 12 characters
#   2. username must not contain spaces
#   3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username cannot be more than 12 characters...")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces...")
elif not username.isalpha():
    print("Your username cannot contain numbers...")
else:
    print(f"Welcome {username}!")
# 4. Nested if
# What is nested if?

# An if statement inside another if statement.

# Example:
# 1. Login System


username = input("Enter user name: ")
password = input("Enter your password: ")

if username == "admin":

    if password == "12345":
        print("Login Successful")
    else:
        print("Invalid password")
else:
    print("Invalide user")


# 2. ATM System
balance = 5000

withdraw = 3000


if withdraw <= balance:

    print("Transaction successful")

else:

    print("Insufficient balance")

# Example 1 Login

try:

    username = input("Username: ")

    if username == "":
        raise ValueError(
            "Username cannot be empty"
        )

except ValueError as e:

    print(e)


# Example 2 Student Marks

try:

    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:

        raise ValueError(
            "Marks must be between 0 and 100"
        )

except ValueError as e:

    print(e)


# Example 3 ATM

class InsufficientBalanceError(Exception):
    pass


balance = 5000

amount = 7000

if amount > balance:

    raise InsufficientBalanceError(
        "Balance too low"
    )
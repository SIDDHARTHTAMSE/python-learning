# Custom Exceptions

# Very Important Interview Topic

# We can create our own exceptions.

# Example 1:

class InvalidAgeError(Exception):
    pass


# Example 2:

class InvalidAgeError(Exception):
    pass


age = 15

if age < 18:

    raise InvalidAgeError(
        "Age must be 18 or above"
    )


# Example 2
# Bank Account

class InsufficientBalanceError(Exception):
    pass


balance = 1000

withdraw = 2000

if withdraw > balance:

    raise InsufficientBalanceError(
        "Insufficient balance"
    )

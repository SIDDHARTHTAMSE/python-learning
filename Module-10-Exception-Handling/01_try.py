# Exception Handling is used to prevent our program from crashing when an error occurs.


# What is an Error?

# An error is a problem in the code that stops execution.

# Example:

# print("Hello"

# Output:

# SyntaxError


# What is an Exception?

# An exception occurs while the program is running.

# Example:

# num = 10

# print(num / 0)

# Output:

# ZeroDivisionError


# Common Exceptions

# ZeroDivisionError
# print(10 / 0)

# ValueError
# age = int("hello")

# TypeError
# print("10" + 10)

# IndexError
# numbers = [1, 2, 3]

# print(numbers[10])
# KeyError
# student = {
#     "name": "Sid"
# }

# print(student["age"])


# try Block

# Syntax:

# try:
#     risky code

# Example:

try:
    print(10 / 0)

except:
    print("Error occurred")
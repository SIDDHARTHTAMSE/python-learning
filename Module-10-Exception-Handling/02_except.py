# except Block

# Used to handle exceptions.

# Example:

try:
    num = int(input("Enter the number: "))

    print(100/num)

except:
    print("Something went wrong")


# Specific Exceptions

# Better practice:

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")


# Example 2:

try:
    age = int("hello")

except ValueError:
    print("Invalid number")


# Example 3:

try:
    numbers = [1,2,3]

    print(numbers[10])

except IndexError:
    print("Index does not exist")


# Multiple Exceptions

# Example:

try:

    num = int(input("Enter number: "))

    print(100 / num)

except ValueError:

    print("Enter numbers only")

except ZeroDivisionError:

    print("Cannot divide by zero")
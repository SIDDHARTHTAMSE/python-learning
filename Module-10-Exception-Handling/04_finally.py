# finally Block
# Runs always.
# Whether exception occurs or not.

# Syntax

# try:
#     code

# except:
#     code

# finally:
#     code


# Example:

try:

    print(10 / 0)

except:

    print("Error")

finally:

    print("Finished")


# Example 2

try:

    print("Hello")

finally:

    print("Finished")


# Real World Example
# Database Connection

try:

    print("Database connected")

except:

    print("Connection failed")

finally:

    print("Database closed")


# Complete Flow

try:

    num = int(input("Enter number: "))

    result = 100 / num

except ValueError:

    print("Invalid input")

except ZeroDivisionError:

    print("Cannot divide by zero")

else:

    print("Result:", result)

finally:

    print("Program ended")
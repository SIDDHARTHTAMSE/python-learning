# else Block
# Runs only if no exception occurs.

# Syntax:

# try:
#     code

# except:
#     code

# else:
#     code

# Example:

try:
    num = int(input("Enter the number: "))

    print(100/num)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Program successful")

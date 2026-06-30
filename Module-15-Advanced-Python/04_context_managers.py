# What is a Context Manager?

# Automatically manages resources.

# Most commonly:

# with
# Without with
# file = open("test.txt", "r")

# print(file.read())

# file.close()

# Need to remember:

# close()
# With with
# with open("test.txt", "r") as file:

#     print(file.read())

# Python closes automatically.


# Example 1
with open("notes.txt", "w") as file:

    file.write("Hello")



# Example 2
with open("notes.txt", "r") as file:

    print(file.read())



# Example 3
with open("data.txt", "a") as file:

    file.write("Python")



# Example 4
with open("student.txt", "w") as file:

    file.write("Sid")
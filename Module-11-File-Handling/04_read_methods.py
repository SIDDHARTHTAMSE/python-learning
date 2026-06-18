# Reading Files
# Python provides 3 methods.


# read()
# Reads entire file.

# Example 1
file = open("student.txt", "r")

print(file.read())

file.close()


# readline()
# Reads one line.

# Example 2

file = open("student.txt", "r")

print(file.readline())

file.close()


# readlines()
# Returns list.

# Example 4

file = open("student.txt", "r")

print(file.readlines())

file.close()
# Why Do We Need File Handling?

# Without file:

name = "Sid"

print(name)

# Output:
# Sid

# After program closes:
# Data Lost ❌

# With file:

# student.txt

# Data remains saved.
# Data Saved Forever ✅

# File Opening

# Python uses:
# open()

# Syntax:

# file = open("filename", "mode")

# Example:

file = open("student.txt", "r")

# File Modes
# r → Read Mode

# Used to read data from file.

# Example 1
# Create file:

# student.txt

# Content:

# Sid
# Rahul
# Amit

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


# Example 2

file = open("student.txt", "r")

print(file.read())

file.close()

# Example 3:

file = open("student.txt", "r")

content = file.read()

print(type(content))

file.close()


# Example 4:

file = open("student.txt", "r")

data = file.read()

print("Sid" in data)

file.close()
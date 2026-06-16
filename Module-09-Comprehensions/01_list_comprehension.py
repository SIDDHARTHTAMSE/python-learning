# Comprehensions are a short and clean way to create:

# Lists
# Dictionaries
# Sets

# 1. List Comprehension
# Syntax
# [new_value for item in iterable]


# What Problem Do Comprehensions Solve?

# Normal way:

numbers = []

for x in range(5):
    numbers.append(x)

print(numbers)


# Comprehension way:
numbers = [x for x in range(5)]
print(numbers)


# Example 2:

# Squares

# Normal:

squares = []

for x in range(1, 6):
    squares.append(x * x)

print(squares)

# Comprehension:

squares = [x * x for x in range(1, 6)]

print(squares)


# Example 3 :

# Even Numbers

evens = [x for x in range(1, 11) if x % 2 == 0]

print(evens)


# Example 4 :

# Odd Numbers

odds = [x for x in range(1, 11) if x % 2 != 0]

print(odds)


# List Comprehension with if

# Example 5:

numbers = [x for x in range(20) if x > 10]

print(numbers)
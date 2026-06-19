# What is a Module?

# Imagine you have a notebook called:

# math_book.py

# Inside it you write:

# def add(a, b):
#     return a + b

# Now instead of writing the add function again and again, you can use it in other files.

# This is called a Module.

# Definition

# A module is a Python file (.py) that contains functions, variables, or classes that can be reused in other programs

# Why Do We Need Modules?

# Without modules:

# # file1.py
# def add(a, b):
#     return a + b

# # file2.py
# def add(a, b):
#     return a + b

# # file3.py
# def add(a, b):
#     return a + b

# Same code repeated everywhere ❌

# With modules:

# # math_utils.py
# def add(a, b):
#     return a + b

# Use everywhere ✅


# Example 1:

import math_utils

print(math_utils.add(10, 20))


# Example 2:

import calculator

print(calculator.multiply(5, 5))



# Example 3:

from maths_utils import add

print(add(45, 5))


# Example 4:

from maths_utils import add, sub

print(add(10, 5))
print(sub(10, 5))
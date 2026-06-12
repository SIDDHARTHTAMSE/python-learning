# This is my first Python program

print("Hello Python")

#1. Single line comments uses "#"
name = "Siddharth"
print(name)

# 2. Multi Line Comment
# Python does not have a special multi-line comment

"""
This program calculates
student marks
"""

# Topic 2: Indentation
# What is indentation?

# Indentation means spaces before code.

# Python uses spaces to understand blocks

# Correct:
if True:
    print("Hello")


# Wrong:
# if True:
# print("Hello")


# Why indentation?

# Other languages use:
# {}

# Example Java:

# if(age>18){
# }


# Example 1:

age = 18

if age >= 18:
    print("You can vote")


# Example 2:

number = 10

if number > 5:
    print("Big Number")
    print("Condition true")


# Example 3
number = 2

if number > 5:
    print("Big")

print("Program finished") 

# It  will give output Because last print is outside if.

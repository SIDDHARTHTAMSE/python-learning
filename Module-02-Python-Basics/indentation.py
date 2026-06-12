# Topic 3: Python Syntax
# What is syntax?
# Syntax means the rules for writing Python code.
# Like English has grammar, Python has syntax rules.


# Colon (:)

# Used after:

# if
# for
# while
# function
# class

# Example:

if age > 18:
    print("Adult")

# Colon says:
# "Next line belongs to this block"



# Indentation
def hello():
    print("Hello")


# No semicolon required
# Other languages:

int age = 20;

# Python:
age = 20


# Example of correct indentation:

def hello():
    print("Hello")

# Here:

# def hello():

# creates a function block.

# The next line:

#     print("Hello")

# has 4 spaces, so Python understands:

# "print Hello is inside the function."


# Wrong indentation example 1
# def hello():
# print("Hello")

# Problem:

# print("Hello") has no spaces.

# Python error:

# IndentationError: expected an indented block


# Wrong indentation example 2
# def hello():
#     print("Hello")

#         print("Bye")

# Problem:

# The second print has extra spaces but it is not inside any block.

# Python error:

# IndentationError: unexpected indent
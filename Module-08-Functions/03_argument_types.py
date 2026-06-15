# Types of Arguments
# 1. Positional Arguments

# Order matters.

# Example:

def student(name, age):
    print(name, age)

student("Sid", 25)


# 2. Keyword Arguments

# Specify parameter names.

# Example:

def student(name, age):
    print(name, age)

student(age=25, name="Sid")


# 3. Default Arguments

# Provide default value.

# Example:

def greet(name="Guest"):
    print("Hello", name)

greet()
# What is a Decorator?

# A decorator is used to add extra functionality to a function without changing the original function.

# Think:

# Gift
#    ↓
# Gift Wrapper

# The gift remains the same.

# Decorator adds extra behavior.


# Example 1
def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper


@decorator
def hello():
    print("Hello")


hello()



# Example 2
def decorator(func):

    def wrapper():
        print("Welcome")

        func()

    return wrapper


@decorator
def student():
    print("Sid")


student()



# Example 3
def decorator(func):

    def wrapper():
        print("Starting")

        func()

        print("Finished")

    return wrapper


@decorator
def run():
    print("Program Running")


run()



# Example 4
def uppercase(func):

    def wrapper():
        return func().upper()

    return wrapper


@uppercase
def greet():
    return "hello"


print(greet())
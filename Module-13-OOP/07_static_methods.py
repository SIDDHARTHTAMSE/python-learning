# Static Methods

# Static methods do not use object data.

# Decorator:

# @staticmethod


# Example 1:
class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))


# Example 2:

class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.multiply(5, 4))
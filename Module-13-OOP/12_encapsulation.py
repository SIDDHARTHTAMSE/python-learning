# Encapsulation
# What is Encapsulation?

# Encapsulation means:

# Wrapping data and methods together.

# Protecting data from direct access.



# Example 1

class Student:

    def __init__(self):
        self.name = "Sid"

s = Student()

print(s.name)


# Example 2

class Bank:

    def __init__(self):
        self.balance = 1000

b1 = Bank()
print(b1.balance)
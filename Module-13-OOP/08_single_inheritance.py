# Inheritance
# What is Inheritance?

# Inheritance means:

# Child gets properties from Parent.

# Real Life Example:

# Father
#     ↓
# Son

# The son gets:

# Surname
# Property
# Business

# Similarly in Python:

# Parent Class
#     ↓
# Child Class

# The child can use everything from the parent


# Single Inheritance

# One parent and one child.



# Example 1

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

d = Dog()

d.sound()


# Example 2

class Person:

    def walk(self):
        print("Walking")

class Student(Person):
    pass

s = Student()

s.walk()
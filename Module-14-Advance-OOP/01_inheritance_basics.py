# What is Inheritance?

# Inheritance means:

# Child gets properties and methods from Parent.

# Real Life Example:

# Father
#    ↓
# Son



# Why Do We Need Inheritance?

# Without inheritance:

# class Dog:

#     def eat(self):
#         print("Eating")


# class Cat:

#     def eat(self):
#         print("Eating")

# Problem:

# Same code repeated ❌



# Parent Class and Child Class
# Parent Class:

class Animal:

    def eat(self):
        print("Eating")

# Child Class:

class Dog(Animal):
    pass



# Example 1 - Basic Inheritance
class Animal:
    
    def eat(self):
        print("Animal is Eating")


class Dog(Animal):
    pass


dog = Dog()

dog.eat()



# Example 2 - Student Example
class Person:

    def walk(self):
        print("Walking")


class Student(Person):
    pass


s = Student()

s.walk()



# Example 3 - Vehicle Example
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):
    pass


car = Car()

car.start()



# Example 4 - Mobile Example
class Mobile:

    def call(self):
        print("Calling...")


class SmartPhone(Mobile):
    pass


phone = SmartPhone()

phone.call()
# What is Abstraction?

# Abstraction means:

# Show Important Things

# Hide Unnecessary Details
# Real Life Example

# Car

# You use:

# Steering
# Brake
# Accelerator

# You don't need to know:

# Engine Internal Parts
# Piston Design
# Fuel Injection Logic



# Abstract Class

# Python provides:

# from abc import ABC, abstractmethod
# Example 1

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Here:
# Animal = Abstract Class

# Example 2
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()


# Example 3
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass



# Example 5

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


c = Car()

c.start()
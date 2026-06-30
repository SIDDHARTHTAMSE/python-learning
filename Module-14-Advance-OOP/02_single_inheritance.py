# Single Inheritance

# One Parent → One Child

# Diagram:

# Animal
#    ↓
#  Dog


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

    def speak(self):
        print("Speaking")


class Teacher(Person):
    pass


t = Teacher()

t.speak()


# Example 3
class Vehicle:

    def fuel(self):
        print("Petrol")


class Car(Vehicle):
    pass


c = Car()

c.fuel()


# Example 4
class Mobile:

    def charge(self):
        print("Charging")


class Android(Mobile):
    pass


a = Android()

a.charge()
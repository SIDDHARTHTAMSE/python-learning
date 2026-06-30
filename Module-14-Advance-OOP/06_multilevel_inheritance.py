# What is Multilevel Inheritance?

# Inheritance chain.

# Real Life Example:

# Grandfather
#      ↓
# Father
#      ↓
# Son

# The son can inherit from father and grandfather.



# Example 1
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Puppy(Dog):
    pass


p = Puppy()

p.eat()



# Example 2
class A:

    def show(self):
        print("Class A")


class B(A):
    pass


class C(B):
    pass


c = C()

c.show()



# Example 3
class Person:

    def walk(self):
        print("Walking")


class Employee(Person):
    pass


class Manager(Employee):
    pass


m = Manager()

m.walk()



# Example 4
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):
    pass


class BMW(Car):
    pass


b = BMW()

b.start()
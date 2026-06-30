# What is Polymorphism?

# The word comes from:

# Poly = Many

# Morph = Forms

# Meaning:

# One Thing → Many Forms


# Why Do We Need Polymorphism?

# Suppose different animals make different sounds.

# Without polymorphism:

# if animal == "dog":
#     print("Bark")

# if animal == "cat":
#     print("Meow")



# Example 1
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()



# Example 2
class Car:

    def move(self):
        print("Drive")


class Plane:

    def move(self):
        print("Fly")


c = Car()
p = Plane()

c.move()
p.move()



# Example 3
class Teacher:

    def work(self):
        print("Teaching")


class Doctor:

    def work(self):
        print("Treating Patients")


t = Teacher()
d = Doctor()

t.work()
d.work()


# Example 4

# Method Overriding is also Polymorphism

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()
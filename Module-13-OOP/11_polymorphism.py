# Polymorphism
# What is Polymorphism?
# One thing → Many Forms

# Same function works differently for different objects.

# Example 1

print(len("Sid"))
print(len([1, 2, 3]))


# Example 2

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


# Example 3

class Car:

    def move(self):
        print("Drive")

class Plane:

    def move(self):
        print("Fly")

c1 = Car()
p1 = Plane()

c1.move()
p1.move()



# Example 4

class Bird:

    def speak(self):
        print("Chirp")

class Human:

    def speak(self):
        print("Hello")

b1 = Bird()
h1 = Human()

b1.speak()
h1.speak()
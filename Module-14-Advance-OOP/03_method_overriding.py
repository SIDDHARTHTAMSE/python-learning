# Method Overriding

# Sometimes the child wants its own version of a parent method.



# Example 1
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()


# Example 2
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def start(self):
        print("Car Started")


c = Car()

c.start()


# Example 3
class Person:

    def introduce(self):
        print("I am a Person")


class Student(Person):

    def introduce(self):
        print("I am a Student")


s = Student()

s.introduce()



# Example 4
class Mobile:

    def show(self):
        print("Basic Mobile")


class SmartPhone(Mobile):

    def show(self):
        print("Android Phone")


m = SmartPhone()

m.show()
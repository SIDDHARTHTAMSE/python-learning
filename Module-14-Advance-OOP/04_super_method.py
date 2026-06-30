# super()

# What if you want:

# Child Method
# +
# Parent Method

# Use:

# super()



# Example 1
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        super().sound()

        print("Bark")


d = Dog()

d.sound()



# Example 2
class Person:

    def show(self):
        print("Person")


class Student(Person):

    def show(self):

        super().show()

        print("Student")


s = Student()

s.show()


# Example 3
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def start(self):

        super().start()

        print("Car Started")

c = Car()
c.start()

    
# Example 4
class Employee:

    def work(self):
        print("Working")


class Manager(Employee):

    def work(self):

        super().work()

        print("Managing")

m = Manager()
m.work()
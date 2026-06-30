# What is Multiple Inheritance?

# Multiple Inheritance means:

# One Child
#    ↑
# Multiple Parents


# Syntax

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass



# Example 1
class Father:

    def property(self):
        print("Father Property")


class Mother:

    def jewellery(self):
        print("Mother Jewellery")


class Child(Father, Mother):
    pass


c = Child()

c.property()
c.jewellery()



# Example 2
class Camera:

    def click(self):
        print("Photo Taken")


class Music:

    def play(self):
        print("Music Playing")


class Phone(Camera, Music):
    pass


p = Phone()

p.click()
p.play()


# Example 3
class Teacher:

    def teach(self):
        print("Teaching")


class Writer:

    def write(self):
        print("Writing")


class Professor(Teacher, Writer):
    pass


p = Professor()

p.teach()
p.write()


# Example 4
class Engine:

    def start(self):
        print("Engine Started")


class GPS:

    def location(self):
        print("Showing Location")


class Car(Engine, GPS):
    pass


c = Car()

c.start()
c.location()
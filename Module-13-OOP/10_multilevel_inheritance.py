# Multilevel Inheritance

# Inheritance chain.

# Grandfather
#     ↓
# Father
#     ↓
# Son


# Example 1

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

p = Puppy()

p.sound()


# Example 4

class Vehicle:

    def start(self):
        print("Started")

class Car(Vehicle):
    pass

class BMW(Car):
    pass

b = BMW()

b.start()
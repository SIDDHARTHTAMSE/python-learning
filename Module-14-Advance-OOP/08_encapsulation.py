# What is Encapsulation?

# Encapsulation means:

# Wrapping Data + Methods Together

# and

# Protecting Data


# Example 1
class Student:

    def __init__(self):
        self.name = "Sid"


s = Student()

print(s.name)



# Example 2
class Student:

    def __init__(self):
        self._name = "Sid"


s = Student()

print(s._name)



# Example 3

class Student:

    def __init__(self):
        self.__marks = 90

    def show_marks(self):
        print(self.__marks)


s = Student()

s.show_marks()


# Example 4

class Bank:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print(self.__balance)


b = Bank()

b.show_balance()
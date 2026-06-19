# Abstraction
# What is Abstraction?

# Show important things.

# Hide implementation details.

# Example:

# Car

# You drive it.

# You don't need to know engine internals.



# Example 1

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass



# Example 2

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
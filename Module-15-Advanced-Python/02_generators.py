# What is a Generator?

# A generator creates values one by one.

# Instead of returning everything at once:

# Return One Value
# Pause
# Return Next Value
# Pause

# Python Uses:

# yield

# Example 1
def numbers():

    yield 1
    yield 2
    yield 3


for n in numbers():
    print(n)



# Example 2
def fruits():

    yield "Apple"
    yield "Mango"
    yield "Banana"


for fruit in fruits():
    print(fruit)



# Example 3
def even_numbers():

    for i in range(2, 11, 2):
        yield i


for num in even_numbers():
    print(num)



# Example 4
def countdown():

    yield 3
    yield 2
    yield 1


for i in countdown():
    print(i)
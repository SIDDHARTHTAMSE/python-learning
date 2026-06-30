# What is an Iterator?

# Iterator allows us to access elements one by one.

# Python uses:

# iter()
# next()


# Example 1
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))


# Example 2
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))



# Example 3
names = ["Sid", "Rahul", "Amit"]

it = iter(names)

print(next(it))



# Example 4
colors = ["Red", "Blue"]

it = iter(colors)

print(next(it))
print(next(it))
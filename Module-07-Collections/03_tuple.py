# Important List Methods
# sort()

numbers = [5,2,8,1]

numbers.sort()
print(numbers)

# reverse()
numbers.reverse()
print(numbers)

# count()
numbers.count(5)
print(numbers)

# clear()
numbers.clear()
print(numbers)


# 2. Tuple
# What is Tuple?

# Tuple is similar to List but cannot be modified.

# Example:

colors = ("Red", "Green", "Blue")
print(colors)


# Access Tuple Items
colors = ("Red", "Green", "Blue")

print(colors[0])


# Tuple Cannot Be Modified
# Wrong:

colors[0] = "Yellow"

# Error:

# TypeError


# Why Use Tuple?

# For fixed values.

# Example:

days = (
    "Monday",
    "Tuesday",
    "Wednesday"
)
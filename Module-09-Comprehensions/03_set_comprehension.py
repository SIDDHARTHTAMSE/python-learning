# 3. Set Comprehension

# Creates sets quickly.

# Syntax
# {
#     value
#     for item in iterable
# }


# Example 1 :

numbers = {
    x
    for x in range(5)
}

print(numbers)


# Example 2

# Squares

squares = {
    x * x
    for x in range(1, 6)
}

print(squares)


# Example 3

# Remove Duplicates

numbers = [1,1,2,2,3,3,4]

unique = {
    x
    for x in numbers
}

print(unique)


# Example 4

# Even Numbers

evens = {
    x
    for x in range(10)
    if x % 2 == 0
}

print(evens)
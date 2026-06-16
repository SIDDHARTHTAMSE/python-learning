# 2. Dictionary Comprehension

# Dictionary comprehension creates dictionaries quickly.

# Syntax
# {
#     key: value
#     for item in iterable
# }


# Example 1:

# Normal Way

square_dict = {}

for x in range(1, 6):
    square_dict[x] = x * x

print(square_dict)


# Dictionary Comprehension

square_dict = {
    x: x * x
    for x in range(1, 6)
}

print(square_dict)


# Example 2:

# Even Numbers Dictionary

numbers = {
    x: x * x
    for x in range(10)
    if x % 2 == 0
}

print(numbers)
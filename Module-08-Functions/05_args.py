# *args

# Used when we don't know how many arguments will be passed.

# Example 1:

def add(*args):
    print(args)

add(10, 20, 30, 40)


# Example 2

def add(*args):

    total = 0

    for num in args:
        total += num

    return total

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
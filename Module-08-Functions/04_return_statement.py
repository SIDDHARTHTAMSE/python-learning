# Return Statement

# Very Important.

# print() displays output.

# return sends output back.


# Without return:

def add():
    print(10 + 20)

add()


# With return:

def add(a, b):
    return a + b

res = add(10, 20)
print(res)


# Example 2

def square(num):
    return num * num

result = square(5)

print(result)


# Example 3

def fullname(first, last):
    return first + " " + last

print(fullname("Sid", "Tamse"))
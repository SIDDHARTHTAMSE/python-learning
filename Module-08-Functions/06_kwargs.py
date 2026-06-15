# **kwargs

# Used when we don't know how many keyword arguments will be passed.

# Example:

def student(**kwargs):
    print(kwargs)

student(
    name="Sid",
    age=25
)


# Example 2

def student(**kwargs):

    for key, value in kwargs.items():

        print(key, value)

student(
    name="Sid",
    age=25,
    city="Mumbai"
)
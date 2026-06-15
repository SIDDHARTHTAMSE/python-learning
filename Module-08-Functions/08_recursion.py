# Recursion

# A function calling itself.

# Very important interview topic.

# Example

def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
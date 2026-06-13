# 4. continue Statement

# Used to skip current iteration.

# Example 1:

for i in range(1, 6):

    if i == 3:
        continue
    print(i)


# Example 2
# Print odd numbers only

for i in range(1, 11):

    if i % 2 == 0:
        continue
    
    print(i)
# 3. elif Statement
# What is elif?

# elif means:

# else if

# Used when we have multiple conditions.

# Syntax:

# if condition:
#     statement

# elif condition:
#     statement

# else:
#     statement



# example
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")
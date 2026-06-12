# 5. Membership Operators

# Checks if a value exists.
# Operators:

# 1.in
# 2.not in

# Example:

name = "Siddharth"
print("d" in name)

numbers = [1,5,8]
print(7 not in numbers)



# 6. Identity Operators

# Checks whether two variables point to the same object.
# Operators:

# is
# is not

# Example:

a = 10
b = 10

print(a is b)



# Practice Programs
# 1. Simple Calculator
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)


# 2. Check Even/Odd
num = 4

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd number")


# 3. Find Greater Number

a = 7
b = 4

if a > b:
    print("a is greater then b")
else:
    print("b is greater then a")


# 4. Calculate Discount
price = 1000
discount = price * 10 / 100
final_price = price - discount
print(final_price)

# 5. Check Login
email = "sidtamse7@gmail.com"
password = "8899"

if email == "sidtamse7@gmail.com" and password == "8899":
    print("Login successfully")
else:
    print("Invalid email or password")
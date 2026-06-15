# 4. Dictionary
# What is Dictionary?

# Stores data as:

# key : value

student = {
    "name": "Sid",
    "age": 25,
    "city": "Mumbai"
}

print(student)


# Access Values
student = {
    "name": "Sid",
    "age": 25
}

print(student["name"])

# Using get()
student = {
    "name": "Sid",
    "age": 25
}

print(student.get("age"))

# Add New Value
student = {
    "name": "Sid",
    "age": 25
}

student["email"] = "sid@gmail.com"
print(student)


# Update Value
student = {
    "name": "Sid",
    "age": 25
}

student["age"] = 26
print(student)


# Delete Value
student = {
    "name": "Sid",
    "age": 25
}

del student["age"]
print(student)

# w → Write Mode
# Used to write data into file.
# ⚠️ Old data gets deleted

# Example 1:

file = open("student.txt", "w")

file.write("Hello Python")

file.close()

# Example 2

file = open("student.txt", "w")

file.write("Sid")

file.close()

# Example 3

file = open("student.txt", "w")

file.write("Python")
file.write(" FastAPI")

file.close()

# Example 4

file = open("student.txt", "w")

file.write("Library Management System")

file.close()
# Writing Files

# Using:
# write()

# Example 1

file = open("notes.txt", "w")

file.write("Python")

file.close()

# Example 2

file = open("notes.txt", "w")

file.write("Python\n")
file.write("FastAPI")

file.close()


# Example 3

file = open("notes.txt", "a")

file.write("\nGitHub")

file.close()


# Example 4

file = open("notes.txt", "a")

file.write("\nDocker")

file.close()
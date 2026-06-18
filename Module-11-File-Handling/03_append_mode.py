# a → Append Mode

# Append means:
# Add at the end

# Old data remains.

file = open("student.txt", "a")

file.write("\nSid")

file.close()

# Example 2

file = open("student.txt", "a")

file.write("\nVijay")

file.close()
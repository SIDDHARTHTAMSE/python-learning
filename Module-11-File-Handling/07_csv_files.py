# CSV Files

# CSV means:

# Comma Separated Values

# Example:

# Name,Age
# Sid,25
# Rahul,22

# Used in Excel and reports


# Example 1 - Write CSV

import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])


# Example 2

    writer.writerow(["Sid", 25])


# Example 3
    writer.writerow(["Rahul", 22])


# Example 4 - Read CSV

import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
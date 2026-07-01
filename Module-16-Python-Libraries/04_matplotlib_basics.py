# 4. Matplotlib
# What is Matplotlib?

# Used for:

# Graphs
# Charts
# Visualization

# Install:
# pip install matplotlib

# Import:
# import matplotlib.pyplot as plt



# Example 1: Basic Line Chart
import matplotlib.pyplot as plt

x = [1, 2, 3]

y = [10, 20, 30]

plt.plot(x, y)

plt.show()



# Example 2: Student Marks
import matplotlib.pyplot as plt

students = ["A", "B", "C"]

marks = [80, 90, 70]

plt.plot(students, marks)

plt.show()



# Example 3: Bar Chart
import matplotlib.pyplot as plt

students = ["A", "B", "C"]

marks = [80, 90, 70]

plt.bar(students, marks)

plt.show()



# Example 4: Pie Chart
import matplotlib.pyplot as plt

data = [30, 40, 30]

plt.pie(data)

plt.show()



# Example 5: Title
import matplotlib.pyplot as plt

x = [1, 2, 3]

y = [5, 10, 15]

plt.plot(x, y)

plt.title("Student Growth")

plt.show()
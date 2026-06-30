# Datetime Module

# Used to work with dates and time.

# Import:
# from datetime import datetime



# Example 1
# Current date and time.

from datetime import datetime

now = datetime.now()

print(now)



# Example 2
# Current year.

from datetime import datetime

now = datetime.now()

print(now.year)



# Example 3
# Current month.

from datetime import datetime

print(datetime.now().month)



# Example 4
# Current day.

from datetime import datetime

print(datetime.now().day)



# Example 5
# Custom format.

from datetime import datetime

print(datetime.now().strftime("%d-%m-%Y"))
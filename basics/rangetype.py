# Range (range) - A sequence of numbers representing an arithmetic progression
r = range(1, 15, 3)  # Creates a range from 1 to 15 with a step of 3
for i in r:
    print(i)

# Output:
# 1
# 4
# 7
# 10
# 13

# Range can be used in various ways, such as iterating through a specific range of numbers.
# It's commonly used in loops, like for loops.

# Creating a range with a different start and end value
r2 = range(5, 10)  # Creates a range from 5 to 9 (10 is exclusive)
for j in r2:
    print(j)

# Output:
# 5
# 6
# 7
# 8
# 9

# Creating a range with a single argument (end value)
r3 = range(5)  # Creates a range from 0 to 4 (5 is exclusive)
for k in r3:
    print(k)

# Output:
# 0
# 1
# 2
# 3
# 4

# Using range in a list
my_list = list(range(3, 9))  # Converts the range to a list
print(my_list)

# Output:
# [3, 4, 5, 6, 7, 8]

# Range objects are memory-efficient, especially for large ranges,
# as they don't store all the numbers in memory at once.

# Negative step in a range
r4 = range(10, 0, -2)  # Creates a range from 10 to 1 with a step of -2
for m in r4:
    print(m)

# Output:
# 10
# 8
# 6
# 4
# 2

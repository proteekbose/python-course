# Flow or Looping Statements in Python

# ----------------------- While Loop -------------------------

# Example 1: Using a while loop to print numbers from 1 to 10
x = 1
while x <= 10:
    print(x)
    x += 1

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Example 2: Using a while loop to print even numbers from 1 to 10
x = 1
while x <= 10:
    if x % 2 == 0:
        print(x)
    x += 1

# Output:
# 2
# 4
# 6
# 8
# 10

# Example 3: Using a while loop to print odd numbers from 1 to 10
x = 1
while x <= 10:
    if x % 2 != 0:
        print(x)
    x += 1

# Output:
# 1
# 3
# 5
# 7
# 9

# Example 4: Using a while loop to calculate the sum of numbers from 1 to 7
x = 1
s = 0
while x <= 7:
    s = s + x
    x += 1
print(s)

# Output: 28

# Example 5: Using a while loop to calculate the sum of squares of numbers from 1 to 5
x = 1
s = 0
while x <= 5:
    s = s + x ** 2
    x += 1
print(s)

# Output: 55

# Example 6: Using a while loop to calculate the factorial of 7
x = 1
p = 1
while x <= 7:
    p = p * x
    x += 1
print(p)

# Output: 5040

# ------------------------------------ For Loop ----------------------------------

# Example 7: Using a for loop to print numbers from 1 to 10
for x in range(1, 11):
    print(x)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Example 8: Using a for loop to calculate the sum of numbers from 1 to 7
s = 0
for x in range(1, 8):
    s = s + x
print(s)

# Output: 28

# Example 9: Using a for loop to calculate the factorial of 7
p = 1
for x in range(1, 8):
    p = p * x
print(p)

# Output: 5040

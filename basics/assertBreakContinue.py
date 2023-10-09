# Assert, Break, and Continue Statements in Python

# ---------------------------------- Assert --------------------------------------

# Example 1: Using the assert statement to check if a number is greater than 10
x = int(input("Enter a number greater than 15: "))
assert x > 15, "Wrong number entered"
print("You entered", x)

# If the entered number is not greater than 10, the program will raise an AssertionError with the message "Wrong number entered."

# ---------------------------------- Break ---------------------------------------

# Example 2: Using the break statement to exit a loop
for x in range(1, 6):
    if x == 3:
        break
    print(x)

# Output:
# 1
# 2

# The loop terminates when x becomes 3, and the break statement is encountered.

# ---------------------------------- Continue ------------------------------------

# Example 3: Using the continue statement to skip an iteration in a loop
for x in range(1, 6):
    if x == 3:
        continue
    print(x)

# Output:
# 1
# 2
# 4
# 5

# The continue statement is used to skip the iteration when x is 3, so it does not print that value.

# Example 4: Using the continue statement to print even numbers
for x in range(1, 11):
    if x % 2 != 0:
        continue
    print(x)

# Output:
# 2
# 4
# 6
# 8
# 10

# In this example, the continue statement is used to skip the iteration when x is odd, allowing only even numbers to be printed.

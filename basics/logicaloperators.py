# Logical Operators in Python

# Logical operators are used to combine multiple conditions and return a Boolean result.

# AND Operator (and)
w = 1
x = 11
y = 15
z = 15

# Example 1: All conditions must be True for the result to be True
print('AND:', w < x and y == z, '[', w < x, ']', '[', y == z, ']')  # Output: AND: True [ True ] [ True ]

# Example 2: If any condition is False, the result is False
print('AND:', w > x and y == z, '[', w > x, ']', '[', y == z, ']')  # Output: AND: False [ False ] [ True ]

# Example 3: If any condition is False, the result is False
print('AND:', w < x and y != z, '[', w < x, ']', '[', y != z, ']')  # Output: AND: False [ True ] [ True ]

# Example 4: If any condition is False, the result is False
print('AND:', w > x and y != z, '[', w > x, ']', '[', y != z, ']')  # Output: AND: False [ False ] [ True ]


# OR Operator (or)

# Example 1: If any condition is True, the result is True
print('OR:', w < x or y == z, '[', w < x, ']', '[', y == z, ']')  # Output: OR: True [ True ] [ True ]

# Example 2: If all conditions are False, the result is False
print('OR:', w > x or y == z, '[', w > x, ']', '[', y == z, ']')  # Output: OR: False [ False ] [ True ]

# Example 3: If any condition is True, the result is True
print('OR:', w < x or y != z, '[', w < x, ']', '[', y != z, ']')  # Output: OR: True [ True ] [ True ]

# Example 4: If all conditions are False, the result is False
print('OR:', w > x or y != z, '[', w > x, ']', '[', y != z, ']')  # Output: OR: False [ False ] [ True ]


# NOT Operator (not)

# Example 1: NOT operator reverses the result of a condition
print('NOT (AND):', not (w < x and y == z), '[', w < x, ']', '[', y == z, ']')  # Output: NOT (AND): False [ True ] [ True ]

# Example 2: NOT operator reverses the result of a condition
print('NOT (OR):', not (w < x or y == z), '[', w < x, ']', '[', y == z, ']')  # Output: NOT (OR): False [ True ] [ True ]


# Example Questions:

a = 11
b = 2
c = 32
d = 10

print('Question 1:', (a <= b) and (b > c))  # Output: Question 1: False
print('Question 2:', (a >= b) or (b != c))  # Output: Question 2: True
print('Question 3:', not ((a != b) and (b > c)))  # Output: Question 3: True
print('Question 4:', not ((a == b) or (b > c)))  # Output: Question 4: False

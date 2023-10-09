# If-Else and Elif Control Statements in Python

# The `if` statement allows you to conditionally execute code blocks based on certain conditions.
# The `elif` statement is used to test multiple conditions.
# The `else` statement is executed when none of the conditions is true.

# Example 1: If-Else Condition
x = 10

if x > 5:
    print('Yes, it is greater.')
else:
    print('No, it is lesser.')

# Output: Yes, it is greater.


# Example 2: If-Elif-Else Condition
x = 9

if x > 11:
    print('Statement 1')
elif x == 5:
    print('Statement 2')
elif x < 8:
    print('Statement 3')
else:
    print('Statement 4')

# Output: Statement 3

# Additional Examples:

# Example 3: Checking if a number is positive, negative, or zero
num = -5

if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')

# Output: Negative

# Example 4: Determining the grade based on marks
marks = 85

if marks >= 90:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
else:
    grade = 'D'

print('Grade:', grade)

# Output: Grade: B

# Example 5: Checking if a number is even or odd
number = 7

if number % 2 == 0:
    print('Even')
else:
    print('Odd')

# Output: Odd

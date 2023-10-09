# Functions in Python

# Functions are blocks of reusable code that perform a specific task.
# They are defined using the `def` keyword.

# Example 1: Defining and using a simple function
def greet(name):
    return "Hello, " + name


message = greet("PyBro")
print(message)


# Output: Hello, PyBro

# Example 2: Function with multiple parameters
def add(a, b):
    return a + b


result = add(5, 3)
print("Result:", result)


# Output: Result: 8

# Example 3: Function with default parameter values
def power(base, exponent=2):
    return base ** exponent


result1 = power(2)
result2 = power(2, 3)

print("Result 1:", result1)
print("Result 2:", result2)


# Output:
# Result 1: 4
# Result 2: 8

# Example 4: Returning multiple values from a function
def calculator(a, b):
    add_result = a + b
    subtract_result = a - b
    multiply_result = a * b
    divide_result = a / b

    return add_result, subtract_result, multiply_result, divide_result


results = calculator(10, 5)
print("Addition:", results[0])
print("Subtraction:", results[1])
print("Multiplication:", results[2])
print("Division:", results[3])


# Output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0

# Example 5: Nested Functions
def greet_with_message(name):
    def message():
        return "Hello"

    def additional_message():
        return "How are you?"

    result = message() + " " + additional_message() + " " + name
    return result


greeting = greet_with_message("PyBro")
print(greeting)

# Output: Hello How are you? PyBro

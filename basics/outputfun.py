# Output Function in Python

# The print function is used to display information on the screen.

# Example 1: Printing full name with and without separator
fname = 'John'
lname = 'Doe'
print(fname, '.', lname, '@example.com')  # Output: John . Doe @example.com
print(fname, '.', lname, '@example.com', sep='')  # Output: John.Doe@example.com

# Example 2: Concatenating strings for output
print(fname + '.' + lname + '@example.com')  # Output: John.Doe@example.com

# Example 3: Printing multiple lines
print()  # Empty line
print("Hello" * 3)  # Output: HelloHelloHello
print("All the power \n is within you")  # Output: All the power
                                        #           is within you

# Example 4: Printing variables with a custom separator
a, b = 10, 20
print(a, b, sep='++++')  # Output: 10++++20

# Example 5: Printing variables with different formatting methods
name = "Alice"
marks = 94.5678

# Using string concatenation
print("Name is", name, "Marks are", marks)  # Output: Name is Alice Marks are 94.5678

# Using the % formatting method (Old-style)
print("Name is %s, Marks are %.3f" % (name, marks))  # Output: Name is Alice, Marks are 94.568

# Using the .format method
print("Name is {}, Marks are {}".format(name, marks))  # Output: Name is Alice, Marks are 94.5678

# Using positional formatting
print("Name is {0}, Marks are {1}".format(name, marks))  # Output: Name is Alice, Marks are 94.5678

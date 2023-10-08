# Integer (int) - Whole numbers without decimal points
a = 42
b = -17
c = 0
print(a, b, c)
print(type(a))

# Float - Numbers with decimal points
x = 3.14159
y = -0.5
z = 2.71828
print(x, y, z)
print(type(z))

# Complex - Numbers with a real and imaginary part
d = 1 + 2j
print(d)
print(type(d))

# Binary Literal - Starting with '0B' or '0b' followed by binary digits (0 and 1)
e = 0B1101
print(e)
print(type(e))

# Hexadecimal Literal - Starting with '0X' or '0x' followed by hexadecimal digits (0-9, A-F)
f = 0X1A3
print(f)
print(type(f))

# Boolean - Represents True or False
g = False
print(g)
print(type(g))
print(5 < 8)  # Comparison results in a boolean value

# Type Conversion
# Converting float to int
h = int(z)
print(h)
print(type(h))

# Converting string to float
i = float("7.5")
print(i)
print(type(i))

# Octal Representation - Using oct() function
decimal_value = 42
print(decimal_value)
print(oct(decimal_value))  # Convert decimal 42 to octal

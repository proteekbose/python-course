# Bytes (bytes) - Immutable sequence of bytes
lst = [65, 66, 67, 68]
print(type(lst))

# Creating a bytes object from a list of integers
b = bytes(lst)
print(type(b))
print(b)

# Attempting to modify a bytes object (uncommenting this line will result in an error)
# b[3] = 22  # TypeError: 'bytes' object does not support item assignment

# Bytearray (bytearray) - Mutable sequence of bytes
b1 = bytearray(lst)
print(type(b1))
print(b1)

# Modifying a bytearray element
b1[2] = 33
print(b1)

# Bytes and bytearrays are often used to represent binary data, such as images or files.

# Creating bytes from a string
str_bytes = bytes("Hello, World!", "utf-8")
print(str_bytes)

# Accessing individual bytes
for byte in str_bytes:
    print(byte)

# Creating a bytearray from a string
str_bytearray = bytearray("Python", "utf-8")
print(str_bytearray)

# Modifying individual characters in a bytearray
str_bytearray[1] = 121  # Changes 'y' to 'y' + 32 (ASCII value)
print(str_bytearray)

# Combining bytes/bytearrays
b2 = bytes([97, 98, 99])
b3 = bytes([100, 101, 102])
combined_bytes = b2 + b3
print(combined_bytes)

ba1 = bytearray([97, 98, 99])
ba2 = bytearray([100, 101, 102])
combined_bytearray = ba1 + ba2
print(combined_bytearray)

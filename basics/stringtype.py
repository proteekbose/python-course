# String (str) - A sequence of characters enclosed in single or double quotes
s = "Hello, Python!"
print(s)

# Multiline String - Enclosed in triple single or double quotes
s1 = """Python is a
powerful programming language.
It's used for various applications."""
print(s1)

# Accessing individual characters in a string
print(s[0])  # Indexing starts from 0, so this prints 'H'

# String repetition
print(s * 3)  # Repeats the string 3 times

# Finding the length of a string
print(len(s1))  # Prints the length of s1
print(len(s))   # Prints the length of s

# String slicing - extracting substrings
print(s[0:5])   # Slice from index 0 to 4 (inclusive), prints 'Hello'
print(s[0:])    # Slice from index 0 to the end, prints the entire string
print(s[:8])    # Slice from the beginning to index 7 (inclusive), prints 'Hello, P'
print(s[-3:-1]) # Slice from the third-to-last character to the second-to-last, prints 'on'

# Slicing with step
print(s[0:9:2])   # Slice from index 0 to 8 with a step of 2, prints 'Hlo,'
print(s[15::-1])  # Reverse the string using slicing, prints '!nohtyP ,olleH'
print(s[::-1])    # Another way to reverse the string

# Removing whitespace from the beginning and end of a string
s = "  You are awesome  "
print(s.strip())   # Removes leading and trailing whitespace
print(s.lstrip())  # Removes leading whitespace
print(s.rstrip())  # Removes trailing whitespace

# Finding substring and counting occurrences
print(s.find("awe", 0, 8))  # Find 'awe' in the first 8 characters, returns -1 if not found
print(s.count("a"))         # Count occurrences of 'a' in the string

# Replacing substrings
print(s.replace("awesome", "super"))  # Replace 'awesome' with 'super' in the string

# String transformations
print(s.upper())  # Convert to uppercase
print(s.lower())  # Convert to lowercase
print(s.title())  # Convert to title case

# Dictionaries (dict) - An unordered collection of key-value pairs
student_scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(student_scores)

# Accessing key-value pairs in a dictionary
print(student_scores.items())

# Iterating through dictionary keys
keys = student_scores.keys()
for key in keys:
    print(key)

# Iterating through dictionary values
values = student_scores.values()
for value in values:
    print(value)

# Accessing a specific value by key
print(student_scores["Charlie"])  # Prints the score for Charlie

# Deleting a key-value pair from a dictionary
del student_scores["Bob"]  # Removes Bob's score from the dictionary
print(student_scores)

# Creating a dictionary with different data types
person_info = {"name": "Alice", "age": 25, "is_student": True}
print(person_info)

# Modifying dictionary values
person_info["age"] = 26  # Updates Alice's age
print(person_info)

# Adding a new key-value pair to a dictionary
person_info["city"] = "New York"  # Adds Alice's city
print(person_info)

# Checking if a key exists in a dictionary
if "age" in person_info:
    print("Age exists:", person_info["age"])

# Dictionary comprehension to create a dictionary
squared_numbers = {x: x ** 2 for x in range(1, 6)}
print(squared_numbers)

# Clearing all key-value pairs from a dictionary
squared_numbers.clear()
print(squared_numbers)  # Outputs an empty dictionary

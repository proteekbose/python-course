# Sets (set) - An unordered collection of unique elements
s = {10, 20, 30, "XYZ", 10, 20, 10}
print(s)

# Accessing the type of the set
print(type(s))

# Adding elements to a set
s.add(5)           # Adds the element 5 to the set
s.update([88, 99]) # Updates the set with elements 88 and 99

print(s)

# Note: Sets do not support repetition, so s * 3 is commented out

# Removing an element from a set
s.remove(30)       # Removes the element 30 from the set

print(s)

# Creating an immutable set (frozenset)
f = frozenset(s)

# Note: Frozensets do not support element removal, so f.remove(20) is commented out

# Performing set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union of sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4}

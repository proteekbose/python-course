# Tuples (tuple) - An ordered, immutable collection of items, which can be of different data types
tpl = (10, 20, 'Alice', -10, 30.5)
print(tpl)

# Accessing elements in a tuple by index
print(tpl[3])     # Accessing the element at index 3, which is -10

# Tuple repetition
print(tpl * 3)    # Repeats the tuple 3 times

# Counting occurrences of an element in a tuple
print(tpl.count(10))  # Counts the number of times 10 appears in the tuple

# Finding the index of an element in a tuple
print(tpl.index('Alice'))  # Finds the index of 'Alice' in the tuple

# Converting a list to a tuple
lst = [67, 34, 'XYZ']
print(type(lst))
tpl1 = tuple(lst)
print(type(tpl1))
print(tpl1)

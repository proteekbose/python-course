# Lists (list) - A collection of items, which can be of different data types
lst = [5, 15, 'Alice', -7, 25.8]
print(lst)

# Accessing elements in a list by index
print(lst[3])     # Accessing the element at index 3, which is -7

# Slicing a list to extract a sublist
print(lst[3:5])   # Slicing from index 3 to 4 (inclusive), prints [-7, 25.8]

# List repetition
print(lst * 4)    # Repeats the list 4 times

# Finding the length of a list
print(len(lst))   # Prints the length of the list

# Adding elements to a list
lst.append(40)    # Appending the value 40 to the end of the list
print(lst)

# Removing elements from a list
lst.remove('Alice')  # Removing the element 'Alice' from the list
del(lst[1])          # Removing the element at index 1
print(lst)

# Clearing the entire list (uncomment to use)
# lst.clear()
# print(lst)

# Finding the maximum and minimum values in a list
print(max(lst))   # Prints the maximum value in the list
print(min(lst))   # Prints the minimum value in the list

# Inserting an element at a specific position
lst.insert(3, 99)  # Inserting the value 99 at index 3
print(lst)

# Sorting a list in descending order
lst.sort(reverse=True)
print(lst)

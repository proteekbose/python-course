# None Data Type
def find_difference(x, y):
    if x == y:
        return None  # Indicating that there is no difference
    else:
        return abs(x - y)  # Calculate and return the absolute difference


result = find_difference(30, 70)

if result is None:
    print("No difference found.")
else:
    print("Difference:", result)


# Escape Sequence Characters
print("Proteek\tBose is \\teaching\tPython")


# Constants (Convention)
PI = 3.14159  # Convention for naming constants
print("The value of PI is:", PI)


# DEL Operator
my_list = [1, 2, 3, 4]
del my_list[1]  # Deletes the element at index 1 (removes 2)
print(my_list)

my_dict = {'USA': 'MA', 'France': 'Paris', 'India': 'Kolkata', 'China': 'Shanghai'}
del my_dict['USA']  # Deletes the 'USA' key-value pair
print(my_dict)

# Immutability (Numbers are immutable)
x = 10
y = 30
z = 10
print(id(x))
print(id(y))
print(id(z))
# x and z have the same value, so they share the same memory location

# However, for mutable types like lists, the id may differ even if the values are the same
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1))
print(id(list2))
# list1 and list2 have the same values but are separate objects

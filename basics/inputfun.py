# Input Function in Python

# The input function allows you to accept user input in Python.

# Example 1: Taking input for name and address
fname = input('Enter firstname:  ')
lname = input('Enter lastname:  ')
city = input('Enter city:  ')
state = input('Enter state:  ')
country = input('Enter country:  ')

print('\n')
print('My full name is', fname, lname,
      'and I live in', city, state, country)

# Note: When you take input from the user, the type is always str.

# Example 2: Taking integer input and performing calculations
num1 = int(input('Enter the first number: '))
print(type(num1))
num2 = int(input('Enter the second number: '))
print(type(num2))

sum_result = num1 + num2
diff_result = num1 - num2

print('Sum:', sum_result)
print('Difference:', diff_result)

# Note: When you make calculations, you may need to convert input to int.

# Example 3: Taking input for a list of numbers
lst_str = input('Enter numbers separated by spaces: ')
lst = [x for x in lst_str.split(' ')]
print('List:', lst)

join_str = ''.join(lst)
print('Join:', join_str)

# Example 4: Taking input for a list of numbers and converting to integers
lst_str = input('Enter numbers separated by spaces: ')
lst = [int(x) for x in lst_str.split(' ')]
print('List:', lst)

sum_result = sum(lst)
print('Sum:', sum_result)

# Example 5: Taking input for a list of floating-point numbers
lst_str = input('Enter three numbers separated by commas: ')
lst = [float(x) for x in lst_str.split(',')]
print('List:', lst)

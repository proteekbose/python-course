# Basic Programs in Python

# Program 1: Find the sum of the first 10 natural numbers.
# 1 + 2 + 3 + ... + 10 = 55

num = 10
s = 0
for x in range(1, num + 1):
    s = s + x
print("Sum of the first", num, "natural numbers:", s)

# Program 2: Find the factorial of a number entered by the user.
# Example: If the user enters 5, the output will be 5! = 120

n = int(input("Please enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial of", n, "is:", factorial)

# Program 3: Check whether a number is even or odd.
# Example: 6 is even, 7 is odd, and 'a' is not a valid input.

n = input("Please enter a number: ")
if n.isalpha():
    print("Invalid input, please enter a valid number.")
else:
    if int(n) % 2 == 0:
        print(n, "is an even number.")
    else:
        print(n, "is an odd number.")

# Program 4: Check whether a number is an Armstrong number or not. An Armstrong number is a number that is equal to
# the sum of its own digits raised to the power of the number of digits. Example: 153 (1^3 + 5^3 + 3^3 = 153) is an
# Armstrong number.

num = int(input("Please enter a number: "))
n = num
sum_of_cubes = 0
while n != 0:
    digit = int(n % 10)
    sum_of_cubes += digit ** 3
    n = n // 10
if sum_of_cubes == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# Program 5: Check whether a number is a palindrome number or not.
# A palindrome number is the same when its digits are reversed.
# Example: 121 is a palindrome number.

num = int(input("Please enter a number: "))
n = num
reversed_num = 0
while n != 0:
    digit = int(n % 10)
    reversed_num = (reversed_num * 10) + digit
    n = n // 10
if reversed_num == num:
    print(num, "is a palindrome number.")
else:
    print(num, "is not a palindrome number.")

# Program 6: Check whether a number is a Harshad number or not.
# A Harshad number is a number that is divisible by the sum of its digits.
# Example: 18 (1 + 8 = 9, and 18 is divisible by 9) is a Harshad number.

num = int(input("Please enter a number: "))
n = num
sum_of_digits = 0
while n != 0:
    digit = int(n % 10)
    sum_of_digits += digit
    n = n // 10
if num % sum_of_digits == 0:
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")



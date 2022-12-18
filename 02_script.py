import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")

import random  #  Python Program to Generate Random Floats
print("Print random number using random.random():")
print(random.random())

#  Python Program to Generate Random Integers random.randint(a, b)
'''
where,
a – starting integer value
b – ending integer value
'''
# Program to generate a random number
# importing the random module
import random

print('Random number:', random.randint(0,10))
print('Random number:', random.randint(0,50))
print('Random number:', random.randint(0,100))
print("Random number", random.randint(-10, 10))
number = random.randint(-5, 5)
if number > 0:
    print(f"The number {number} is positive")
elif number == 0:
    print(f"The number {number} is zero")
elif number < 0:
    print(f"The number {number} is negative")
else:
    print(f"The number {number} is invalid")

# Python Program to Generate Random Number from a List and a String
'''
The syntax is as follows:
random.choice(iterable)
where,
iterable – a sequence of list, tuple or a string
If the iterable passed to random.choice() is empty, 
Python interpreter will raise an exception.
'''
# Python program to illustrate choice() method
import random
# prints a random value from the list
list1 = [3, 5, 6, 4, 7, 11, 13]
print("Random number from list: ",random.choice(list1))
# prints a random item from the string
string = '9674271903'
print("Random number from string: ", random.choice(string))

"""Print the alphabet in lowercase and uppercase, 
not followed by a new line using the ASCII method"""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="|")
print('\n')
for letter in range(65, 91):
    print("{}".format(chr(letter)), end= "|")
print()

"""
Syntax:
ascii(object)
Parameters:
object: Any type of object.
Return type:
Returns a string.
The ascii() method returns a printable carriage return character in a string, as shown below.
"""
# Example: ascii()
mystr='''this
is a new line.'''
print(ascii(mystr))
"""
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

Print all the letters except q and e
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
"""
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end=" | ")
print()

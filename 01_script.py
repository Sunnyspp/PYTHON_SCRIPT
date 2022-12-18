topic ='''
FUNCTIONS IN PYTHON
'''
print(topic, end="")
definition = '''
A function is a set of statement that take inputs, do some specific computation and produces output.
'''
print(definition, end="")

# A simple python program to check
# whether a number is even or odd.

number = eval(input("Enter a number: "))
def evenOdd(number):
    if (number % 2 == 0):
        print("The number is EVEN")
    else:
        print("The number is ODD")
# test code by calling the function
evenOdd(number)

num1 = eval(input("Enter num1: "))
num2 = eval(input("Enter num2: "))
op = input("Enter one of +, -, *, /, %: ")

def calculator (num1, num2):
    if op == '+':
       result = num1 + num2
       print(f"{num1}+{num2} = {result}")
    elif op == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif op == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif op == '/':
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    elif op == '%':
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print('invalid Operator: Enter a valid operator')

calculator(num1, num2)

def replace_index(x):
    x[0] = 20

index_list = [10, 13, 17, 22, 27]
replace_index(index_list)
print(index_list)

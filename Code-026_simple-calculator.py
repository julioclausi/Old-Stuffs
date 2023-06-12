#Functions

def add (a,b):
    return a + b

def subtract (a,b):
    return a - b

def divide (a,b):
    return a / b

def multiply (a,b):
    return a * b

operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}

num1 = int(input('Digit the first number: '))
num2 = int(input('Digit the second number: '))
op = input('Digit the operation + - * /: ')
calc_function = operations[op]

print (f'{num1} {op} {num2} = {calc_function(num1,num2)}')
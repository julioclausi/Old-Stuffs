#Let's try to calculate the factorial of an integer

number = input('Digit a number: ')
factorial_number = 1
for i in range(1,int(number)+1):
    factorial_number = factorial_number * i

print (f'{number}! = {factorial_number}')

#Now using a recursive function
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

print (f'Factorial of the number {number} is {factorial(int(number))}')
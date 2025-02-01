import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letters = int(input('Digit a number of letters: '))
number_of_numbers = int(input('Digit a number of numbers: '))
number_of_symbols = int(input('Digit a number of symbols: '))

password = []

for count in range(0,number_of_letters):
    password += random.choice(letters)

for count in range(0,number_of_numbers):
    password += random.choice(numbers)

for count in range(0,number_of_symbols):
    password += random.choice(symbols)

random.shuffle(password)

my_pwd = ""
for char in password:
    my_pwd += char

print (f'Your passowrd is: {my_pwd}')
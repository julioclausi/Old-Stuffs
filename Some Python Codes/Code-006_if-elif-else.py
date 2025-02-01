#Let's make a program that asks the user for a number
#and we show if it is even, odd or not a number

#Asking for a number
my_number = input ('Please, digit an integer number: ')

#Let's check if the user entered a number
if my_number.isdigit():
    print (f'The number {my_number} is ',end='')
    if int(my_number) % 2 == 0:
        print('Even')
    else:
        print('Odd')
    #print (f'Number is {"Even" if int(my_number) % 2 == 0 else "Odd"}')
    #This works too
    #But is not so clean
else:
    print ('This is not an integer number!')

#Let's try with if elif and else
if not my_number.isdigit():
    print ('This is not an integer number!')
elif int(my_number) % 2 == 0:
    print ('Even')
else:
    print ('Odd')

#Let's study input

my_input = input('Digit something: ')
print (f'Type: {type(my_input)}') #Type: <class 'str'>

#So, input always return a str

print (my_input.isdigit()) #True (if the user input a int) or False 

#I can use a method called isdigit to check if the user input a str or an int
#This could be nice for a calculator or something else

if my_input.isdigit():
    print ('This is a number', my_input)
else:
    print ('This is not a number', my_input)
#Let's work with some numbers

number_1 = 123
print (number_1) #123
print (type(number_1)) #<class 'int'>
#print(len(number_1)) ---> TypeError: object of type 'int' has no len()

number_2 = 0.456
print (number_2) #0.456 
print (type(number_2)) #<class 'float'>
#print(len(number_2)) ---> TypeError: object of type 'float' has no len()

#Can I add an integer and a float number?
number_3 = number_1 + number_2
print (number_3) #123.456 
print (type(number_3)) #<class 'float'>

number_1 = 10
number_2 = 5
print ('a + b =', number_1 + number_2) #15
print ('a - b =', number_1 - number_2) #5
print ('a * b =', number_1 * number_2) #50
print ('a / b =', number_1 / number_2) #2.0
#A division returns a float

number_1 = 7
number_2 = 2
print ('a ** b =', number_1 ** number_2) #49
#Power
print ('a / b =', number_1 / number_2) #3.5
print ('a // b =', number_1 // number_2) #3
print ('a %% b =', number_1 % number_2) #1
#Mod

#Can I add a str and a int?
my_int = 1
my_str = '1'
#So, 1+1=2, ain't?
#my_result = my_int + my_str ---> TypeError: unsupported operand type(s) for +: 'int' and 'str'
#So, let's try to transform the str in an int
my_str_becomes_an_int = int(my_str)
my_result = my_int + my_str_becomes_an_int
print (my_result) #2
#Let's try some loops

#I want to ask the user for Q or B
#If Q, the code will change the variable my_loop to False
#If B, the code will break the while
#Else, the code will stand at the loop
my_loop = True
while my_loop:
    user_input = input ('[Q]uit [B]reak: ')
    if user_input.lower() == 'q':
        print ('Quit')
        my_loop = False
    elif user_input.lower() == 'b':
        print ('Break')
        break
    else:
        continue

for something in range (0,10):
    print (something+1,end=' ') #1 2 3 4 5 6 7 8 9 10
print ()

for something in range (0,10,2):
    print (something,end=' ') #0 2 4 6 8
print ()

for letter in 'My Text':
    print(letter,end='')
print ()
#For is amazing
#Works more like an iterator method as found in other OOP languages
#Let's try code a game
#a simple game
#There is a word
#and the user has to figure out which word is
#the program will ask letter by letter

#let's try the word 'banana'
#the program will show '******'
#if the user try the letter 'a' the program will show '*a*a*a'
#until the user discover the secret word

#Why banana? https://www.youtube.com/watch?v=wCkerYMffMo

secret_word = 'banana' #the secret word
password = '' #a var that I use to check what the user tried
aux_password = '' #another aux var
for i in secret_word:
    password += '*' #creating the **** pass

won = False #a bool to check if the user won

while not won:
    print (password)
    letter = input ('Digit a letter: ')
    count=0
    aux_password = password + '' #I have to do that, because when I tried withou the "+ ''" the aux_password were receiving the address of password
    password = '' #And when I did that it changed aux_password too

    #This for is used to check letter by letter of secret_word and when the user hit one word that exists in the secret_word
    #the code put the letter in the place of a *
    for i in secret_word:
        if letter == i:
            password += i
        else:
            password += aux_password[count]
        count += 1
    
    #Here I check if the user hit the letter
    if password == aux_password:
        print ('Try again another letter')

    #Here I check if the user hit the word
    if password == secret_word:
        print ('You Win!')
        won=True

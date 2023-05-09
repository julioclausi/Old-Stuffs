#A program that checks if CPF is valid
#CPF is a 11 digit number used in Brazil
#the last two digits are the first and the second verification numbers
#XXX.XXX.XXX-XX

my_cpf = input ('Digit CPF: ')

if len(my_cpf) == 11 and my_cpf.isdigit():
    #Check First Verification Digit
    multiplier=10
    my_sum=0
    for number in range(0,9):
        my_sum = my_sum + (int(my_cpf[number])*multiplier)
        multiplier -= 1
    result_division = my_sum // 11
    result_mod = my_sum % 11
    if result_mod < 2:
        first_digit = 0
    else:
        first_digit = 11 - result_mod
    if first_digit == int(my_cpf[9]):
        print ('First validation digit OK')
        #Check Second Verification Digit
        multiplier = 11
        my_sum = 0
        for number in range(0,10):
            my_sum = my_sum + (int(my_cpf[number])*multiplier)
            multiplier -= 1
        result_mod = my_sum % 11
        if result_mod < 2:
            second_digit = 0
        else:
            second_digit = 11 - result_mod
        if second_digit == int(my_cpf[10]):
            print ('VALID CPF!')
        else:
            print ('Second validation digit does not match!')
    else:
        print ('First validation digit does not match!')
else:
    print ('Not a 11 digit CPF!')
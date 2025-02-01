import os
from time import sleep
import random

def printing(my_list):
    sleep(0.5)
    os.system('cls')
    for value in my_list:
        to_print = "|" + ("-"*value) + "|"
        print(f'{value:^5}:{to_print:^50}')

def bubblesort(my_list):
    for i in range (len(my_list)-1,0,-1):
        for j in range(0,i):
            if my_list[j] > my_list[j+1]:
                aux = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = aux
                printing(my_list)

my_list = random.sample(range(0,30),15)
print(my_list)
input('Press [Enter] to start')
printing(my_list)
bubblesort(my_list)
print(my_list)
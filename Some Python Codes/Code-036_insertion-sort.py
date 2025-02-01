import os
from time import sleep
import random

def printing(my_list):
    sleep(1)
    os.system('cls')
    for value in my_list:
        to_print = "|" + ("-"*value) + "|"
        print(f'{value:^5}:{to_print:^50}')

def insertionsort(my_list):
    for i in range(1,len(my_list)):
        key = my_list[i]
        j = i-1
        while j>=0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j-=1
        my_list[j+1] = key
        printing(my_list)

my_list = []

for i in range(1,40,2):
    my_list.append(i)

random.shuffle(my_list)

print(my_list)
input('Press [Enter] to start')
printing(my_list)
insertionsort(my_list)
print(my_list)
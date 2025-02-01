import os
from time import sleep
import random

def printing(my_list):
    sleep(1)
    os.system('cls')
    for value in my_list:
        to_print = "|" + ("-"*value) + "|"
        print(f'{value:^5}:{to_print:^50}')

def selectsort(my_list):
    for i in range(len(my_list)):
        min = i
        for j in range(i+1,len(my_list)):
            if my_list[min] > my_list[j]:
                min = j
        if my_list[min] != my_list[i]:
            aux = my_list[min]
            my_list[min] = my_list[i]
            my_list[i] = aux
            printing(my_list)

my_list = []

for i in range(1,40,2):
    my_list.append(i)

random.shuffle(my_list)

print(my_list)
input('Press [Enter] to start')
printing(my_list)
selectsort(my_list)
print(my_list)
import os
from time import sleep
import random

def printing(myList):
    sleep(0.25)
    os.system('cls')
    print(myList)
    for number in myList:
        print(f'{number*"-":^30}')

def bubbleSort(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                # aux = A[j]
                # A[j] = A[j+1]
                # A[j+1] = aux
            printing(A)

myList = [i for i in range(1,30,2)]
random.shuffle(myList)

bubbleSort(myList)

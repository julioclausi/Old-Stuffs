import os
from time import sleep
import random

def printing(myList):
    sleep(0.5)
    os.system('cls')
    print(myList)
    for number in myList:
        print(f'{number*"-":^30}')

def insertionSort(myList):
    for i in range(1,len(myList)):
        number = myList[i]
        j = i - 1
        while (j>=0) and (myList[j] > number):
            myList[j+1] = myList[j]
            myList[j] = number
            j -= 1
            printing(myList)

myList = [i for i in range(1,30,2)]
random.shuffle(myList)
insertionSort(myList)

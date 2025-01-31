import os
from time import sleep
import random

def printing(myList):
    sleep(0.5)
    os.system('cls')
    print(myList)
    for number in myList:
        print(f'{number*"-":^30}')

def merge(A,inicio,fim):
    meio = int((inicio + fim) / 2)
    esquerda = A[inicio:meio+1]
    direita = A[meio+1:fim+1]
    i = 0
    j = 0
    k = inicio
    while i<len(esquerda) and j<len(direita):
        if esquerda[i] <= direita[j]:
            A[k] = esquerda[i]
            i+=1
        else:
            A[k] = direita[j]
            j+=1
        k+=1
        printing(A)

    while i<len(esquerda):
        A[k] = esquerda[i]
        k+=1
        i+=1
    while j<len(direita):
        A[k] = direita[j]
        k+=1
        j+=1

def mergeSort(A,inicio,fim):
    if (inicio >= fim):
        return
    meio = int((inicio + fim) / 2)
    mergeSort(A,inicio,meio)
    mergeSort(A,meio+1,fim)
    merge(A,inicio,fim)

myList = [i for i in range(1,30,2)]
random.shuffle(myList)
print(myList)
mergeSort(myList,0,len(myList)-1)
print(myList)

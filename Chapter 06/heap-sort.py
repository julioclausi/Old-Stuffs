def esquerda (i):
    return i*2 + 1

def direita (i):
    return i*2 + 2

def pai (i):
    return int((i-1)/2)

def maximizaHeap (A,i):
    esq = esquerda(i)
    dir = direita(i)
    tam = len(A)
    if (esq <= tam) and (A[esq] > A[i]):
        maior = esq
    else:
        maior = i
    if (dir <= tam) and (A[dir] > A[maior]):
        maior = dir
    if maior != i:
        A[maior], A[i] = A[i], A[maior]
        maximizaHeap(A,maior)

myArray = [16,4,10,14,7,9,3,2,8,1]
print(myArray)
maximizaHeap(myArray,1)
print(myArray)

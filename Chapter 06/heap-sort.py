def esquerda (i):
    return i*2 + 1

def direita (i):
    return i*2 + 2

def pai (i):
    return int((i-1)/2)

def constroiMaxHeap(A):
    primeiraFolha = int(len(A)/2)
    ultimoNodo = primeiraFolha-1
    for i in range(ultimoNodo, -1, -1):
        print(i)
        maximizaHeap(A,i)

def maximizaHeap (A,i):
    esq = esquerda(i)
    dir = direita(i)
    tam = len(A)
    if (esq < tam) and (A[esq] > A[i]):
        maior = esq
    else:
        maior = i
    if (dir < tam) and (A[dir] > A[maior]):
        maior = dir
    if maior != i:
        A[maior], A[i] = A[i], A[maior]
        maximizaHeap(A,maior)

# myArray = [16,4,10,14,7,9,3,2,8,1]
myArray = [4,1,3,2,16,9,10,14,8,7]
print(myArray)
constroiMaxHeap(myArray)
print(myArray)

def esquerda (i):
    return i*2 + 1

def direita (i):
    return i*2 + 2

def pai (i):
    return int((i-1)/2)

def constroiMaxHeap(A,tamanho):
    primeiraFolha = int(tamanho/2)
    ultimoNodo = primeiraFolha-1
    for i in range(ultimoNodo, -1, -1):
        maximizaHeap(A,i,tamanho)

def maximizaHeap (A,i,tamanho):
    esq = esquerda(i)
    dir = direita(i)
    tam = tamanho
    if (esq < tam) and (A[esq] > A[i]):
        maior = esq
    else:
        maior = i
    if (dir < tam) and (A[dir] > A[maior]):
        maior = dir
    if maior != i:
        A[maior], A[i] = A[i], A[maior]
        maximizaHeap(A,maior,tamanho)

def heapSort (A):
    qtdDeItens = len(A)
    constroiMaxHeap(A, qtdDeItens) # O(n)
    for i in range(qtdDeItens-1,0,-1):
        A[i], A[0] = A[0], A[i]
        qtdDeItens-=1
        maximizaHeap(A,0,qtdDeItens) # O(lgn)
        # portanto será O(n lgn)

# myArray = [16,4,10,14,7,9,3,2,8,1]
# myArray = [4,1,3,2,16,9,10,14,8,7]
myArray = [9,8,7,6,5,4,3,2,1]
print(myArray)
heapSort(myArray)
print(myArray)

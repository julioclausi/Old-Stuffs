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

array = [6,5,7,4,1,8,3,2]
print(array)
mergeSort(array,0,len(array)-1)
print(array)

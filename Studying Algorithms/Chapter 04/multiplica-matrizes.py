# qualquer matriz multiplicada por uma matriz identidade
# será igual a própria matriz
def multiplicaMatriz (A,B,C):
    tamanho = len(A)
    for i in range(0,tamanho):
        for j in range(0,tamanho):
            for k in range(0,tamanho):
                C[i][j] += (A[i][k] * B[k][j])

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

C = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

print(A)
print(B)
multiplicaMatriz(A,B,C)
print(C)

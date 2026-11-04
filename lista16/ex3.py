n = int(input())

matriz = []

linhaN = []

linhaN.extend(int(input().split()))

matriz[0] = linhaN

for i in range(1, n):
    n -= 1
    for j in range(n):
        if matriz[i][j - 1] + matriz[i + 1][j - 1] == 0:
            matriz[i][j] = -1
        else:
            matriz[i][j] = 1

#terminar depois
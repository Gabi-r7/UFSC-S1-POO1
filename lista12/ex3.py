import random

ordem = int(input('Digite a ordem da matriz: '))
l = int(input('Digite a linha para a opereação: '))
op = input('S ou M: ').upper()

l -= 1

matriz = [[random.randint(1, 100) for _ in range(ordem)] for _ in range(ordem)]

for linha in matriz:
    print(linha)

resultado = 0
for i in range(ordem):
    for j in range(ordem):
        if l == i:
            if op == 'S':
                resultado += matriz[i][j]
            elif op == 'M':
                resultado += matriz[i][j] / ordem

print(resultado)

import random

ordem = int(input('Digite a ordem da matriz: '))
aleatorio = int(input('Deseja preencher a matriz aleatoriamente? (1 para sim): '))
op = input('S ou M: ').upper()

matriz = list()

if aleatorio == 1:
    matriz = [[random.randint(1, 100) for _ in range(ordem)] for _ in range(ordem)]
else:
    for i in range(ordem):
        for j in range(ordem):
            aux = int(input())
            matriz[i][j].append(aux)

for linha in matriz:
    print(linha)

cont = 0
resultado = 0
for i in range(ordem):
    for j in range(ordem):
        if i > j:
            resultado += matriz[i][j]
            cont += 1

if op == 'S':
    print(resultado)
else:
    print(f'{resultado/cont:.1f}')

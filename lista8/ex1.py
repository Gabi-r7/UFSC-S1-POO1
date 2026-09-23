n = int(input('n: '))
k = int(input('k: '))

lista = list()

for i in range(n):
    lista.append(int(input(f'lista[{i}]: ')) * k)

for i in lista:
    print(i)

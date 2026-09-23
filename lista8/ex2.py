n = int(input('n: '))
lista = []
iguais = []

for i in range(n):
    lista.append(int(input(f'lista[{i}]: ')))

    for j in range(i):
        if lista[i] == lista[j]:
            iguais.append(lista[i])

for i in iguais:
    print(i)

numeros = list()
pares = list()
impares = list()

for i in range(10):
    aux = int(input())

    if aux % 2 == 0:
        pares.append(aux)
    else:
        impares.append(aux)

numeros.append(sorted(pares))
numeros.append(sorted(impares))

print(numeros)

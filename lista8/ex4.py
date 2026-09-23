quant_numeros = 10

lista = []
pos_maior, maior, pos_menor, menor = 0, 0, 0, 0
existe = False

for i in range(quant_numeros):
    while True:
        existe = False
        lista.append(int(input(f'Digite o número para a {i}° posição: ')))

        for j in range(i):
            if lista[j] == lista[i]:
                print('Esse número já existe! Digite novamente!')
                existe = True
                lista.pop()
                break

        if not existe:
            break

    if i == 0:
        maior = lista[i]
        menor = lista[i]
        pos_maior = i
        pos_menor = i
    elif lista[i] > maior:
        maior = lista[i]
        pos_maior = i
    elif lista[i] < menor:
        menor = lista[i]
        pos_menor = i

print(f'Maior: {maior} na posição {pos_maior}')
print(f'Menor: {menor} na posição {pos_menor}')

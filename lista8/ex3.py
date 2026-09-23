notas = []
quant_notas = 5
maior_nota = 0
menor_nota = 10

for i in range(quant_notas):
    notas.append(float(input(f'Digite a {i+1}° nota: ')))

    if notas[i] > maior_nota:
        maior_nota = notas[i]
    if notas[i] < menor_nota:
        menor_nota = notas[i]

print(f'Maior nota: {maior_nota}\nMenor nota: {menor_nota}\nDiferença: {maior_nota - menor_nota}')

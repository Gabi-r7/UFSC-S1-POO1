maior, meio, menor = 0, 0, 0

for i in range(1, 4):
    num = int(input(f'Digite o {i}° número: '))

    if i == 1:
        maior = num
    elif num > maior:
        menor = meio
        meio = maior
        maior = num
    else:
        if num > meio:
            menor = meio
            meio = num
        else:
            menor = num

print(f'A ordem dos números é: {maior} > {meio} > {menor}')
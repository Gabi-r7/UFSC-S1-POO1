pares, impares = 0, 0

for i in range(10):
    num = int(input('Digite um número inteiro: '))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Foram digitados {pares} números pares e {impares} números ímpares')

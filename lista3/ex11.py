n = int(input('Digite a quantidade de números a serem lidos: '))
media, maior, menor = 0, 0, 0

for i in range(n):
    num = int(input('Digite um número: '))
    media += num

    if num > maior:
        maior = num
    if num < menor:
        menor = num

media /= n

print(f'Média: {media:.2f}\nMaior número: {maior}\nMenor número: {menor}')

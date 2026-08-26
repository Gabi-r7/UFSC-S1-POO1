import random

aleatorio = random.randint(0, 10)

while True:
    chute = int(input('Digite seu chute: '))

    if chute < aleatorio:
        print('O número gerado é maior')
    elif chute > aleatorio:
        print('O número gerado é menor')
    else:
        print('Você acertou!')
        break

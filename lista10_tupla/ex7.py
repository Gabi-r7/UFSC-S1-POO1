while True:
    n = int(input())

    if n == 0:
        break

    suspeitos = list()
    maior = 0
    segundo_maior = 0
    
    suspeitos.extend(map(int, input().split()))

    for i in range(len(suspeitos)):
        if suspeitos[i] > maior:
            segundo_maior = maior
            maior = suspeitos[i]
        elif suspeitos[i] > segundo_maior:
            segundo_maior = suspeitos[i]

    print(suspeitos.index(segundo_maior) + 1)

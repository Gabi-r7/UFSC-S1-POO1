duracoes = {
    'W': 64,
    'H': 32,
    'Q': 16,
    'E': 8,
    'S': 4,
    'T': 2,
    'X': 1
}

while True:
    composicao = input()

    if composicao == '*':
        break

    compassos = composicao.split('/')
    corretos = 0

    for compasso in compassos:
        if compasso == '':
            continue

        duracao = 0

        for nota in compasso:
            duracao += duracoes[nota]

        if duracao == 64:
            corretos += 1

    print(corretos)
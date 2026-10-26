
while True:
    n = int(input())

    if n == 0:
        break

    alunos = {}
    falsos = 0

    for _ in range(n):
        nome, assinatura = map(str, input().split())
        alunos[nome] = assinatura

    m = int(input())

    for _ in range(m):
        nome, assinatura = map(str, input().split())
        original = alunos[nome]
        diferentes = 0

        menor_tamanho = min(len(original), len(assinatura))

        for i in range(menor_tamanho):
            if original[i] != assinatura[i]:
                diferentes += 1

        diferentes += abs(len(original) - len(assinatura))

        if diferentes > 1:
            falsos += 1

    print(falsos)

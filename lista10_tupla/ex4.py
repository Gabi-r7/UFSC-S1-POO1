n = int(input('Casos teste: '))

for i in range(n):
    quant_alunos, secreto = map(int, input().split())
    qt = []
    qt.extend(map(int, input().split()))
    mais_proximo = qt[0]
    ganhador = 0

    for j in range(len(qt)):
        if abs(secreto - qt[j]) < abs(secreto - mais_proximo):
            mais_proximo = qt[j]
            ganhador = j + 1

    print(ganhador)

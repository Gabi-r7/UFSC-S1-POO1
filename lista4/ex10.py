n = int(input('Digite a quantidade de casos: '))

while n > 0:
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x

    soma = 0
    valor = x + 1
    while valor < y:
        if valor % 2 != 0:
            soma += valor
        valor += 1

    print(soma)
    n -= 1

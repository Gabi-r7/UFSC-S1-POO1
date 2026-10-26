m, n = map(int, input().split())

palavras = {}

for i in range(m):
    palavra, valor = input().split()
    palavras[palavra] = int(valor)

for i in range(n):
    salario = 0

    while True:
        linha = input()

        if linha == '.':
            break

        palavras_da_linha = linha.split()

        for palavra in palavras_da_linha:
            if palavra in palavras:
                salario += palavras[palavra]

    print(salario)

n = int(input())

for i in range(n):
    produtos = {}
    preco = 0

    m = int(input())
    for j in range(m):
        nome, valor = map(str, input().split())
        produtos.update({nome: float(valor)})

    quantidadeProdutos = int(input())

    for k in range(quantidadeProdutos):
        nome, quant = map(str, input().split())
        preco += produtos[nome] * int(quant)

    print(f'R$ {preco}')

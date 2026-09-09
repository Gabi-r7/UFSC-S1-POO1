# Gabriel Henrique Lamb
# 26205861

def verificaEntrada(aux1, n, aux2):
    while not (aux1 <= n <= aux2):
        n = int(input('Valor não suportado! Digite novamente: '))

    return n

def main():
    dias, saldo = map(int, input('Digite a quantidade de dias e o saldo inicial: ').split())
    dias = verificaEntrada(1, dias, 30)
    saldo = verificaEntrada(-1000, saldo, 1000)

    
    for i in range(dias):
        movimentacao = int(input('Digite o valor movimentado: '))
        saldo += movimentacao

        if i == 0:
            menorSaldo = saldo
        elif saldo < menorSaldo:
            menorSaldo = saldo

    print(menorSaldo)

main()

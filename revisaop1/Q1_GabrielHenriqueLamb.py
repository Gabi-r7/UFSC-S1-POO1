# Gabriel Henrique Lamb
# 26205861

def verificaEntrada(consumo):
    while not (0 <= consumo <= 1000):
        print('Valor fora do limite.')
        consumo = int(input('Digite o consumo novamente (em m³): '))

    return consumo


def calculaValorConta(consumo):

    if consumo <= 10:
        valorConta = 7
    elif 10 < consumo <= 30:
        valorConta = 7 + (1 * (consumo - 10))
    elif 30 < consumo <= 100:
        valorConta = 27 + (2 * (consumo - 30))
    elif 100 < consumo:
        valorConta = 167 + (5 * (consumo - 100))

    return valorConta

def main():
    continuar = 'S'

    while continuar != 'N':

        consumo = int(input('Digite o consumo (em m³): '))

        consumo = verificaEntrada(consumo)
        formaPagamento = int(input('Digite a opção de pagamento:\n1 - Dinhero\n2 - Pix\n3 - Cartão\nInforme sua escolha: '))

        valorConta = calculaValorConta(consumo)

        print(f'Valor da conta: R${valorConta:.2f}')
        
        if formaPagamento == 1:
            valorConta = valorConta - (valorConta * (5 / 100))
            print(f'Valor com desconto: R${valorConta:.2f}')

        continuar = input('Deseja continuar (S/N): ').upper()

    print('Programa encerrado')

main()

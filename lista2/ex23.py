
while True:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    if valor1 == valor2:
        print('Erro! Valores iguais. Digite novamente os valores')
    elif valor1 < 0 or valor2 < 0 or valor1 > 1000 or valor2 > 1000:
        print('Erro! Valores fora do intervalo (0 a 1000). Digite novamente os valores')
    elif valor1 > valor2:
        print(f'Triplo do maior é {valor1 * 3}')
        break
    else:
        print(f'Triplo do maior é {valor2 * 3}')
        break

valor_casa = float(input('Digite o valor da casa: '))
salario_comprador = float(input('Digite o valor do salário do comprador: '))
anos_pagamento = int(input('Digite em quantos anos será pago (em anos): '))

prestacao_mensal = valor_casa / (anos_pagamento * 12)


if prestacao_mensal > salario_comprador * 0.3:
    print(f'O empréstimo foi negado pois excederá 30%. Prestação seria de R${prestacao_mensal:.2f}')
else:
    print(f'O empréstimo foi aprovado! Valor da prestação mensal é de R${prestacao_mensal:.2f}')

valor_produto = float(input('Digite o valor do produto: '))
condicao_pagamento = input('a - À vista (dinheiro ou cheque) - 10%\nb - 1x no cartão - 5%\nc - 2x no cartão - preço normal\nd - 3x ou mais no cartão - 20% de juros\n Escolha sua opção: ')

if condicao_pagamento == "a":
    print(f'Valor do produto ficou R${valor_produto - valor_produto * 0.1:.2f}')
elif condicao_pagamento == "b":
    print(f'Valor do produto ficou R${valor_produto - valor_produto * 0.05:.2f}')
elif condicao_pagamento == "c":
    print(f'Nenhum desconto foi considerado! Valor do produto: R${valor_produto:.2f}')
elif condicao_pagamento == "d":
    print(f'20% de juros acrescido no valor. Resultando em R${valor_produto + valor_produto * 0.2:.2f}')
else:
    print('Erro na escolha')

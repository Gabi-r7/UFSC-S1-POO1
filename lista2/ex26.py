preco = float(input('Digite o preço do produto: R$ '))
valor_pago = float(input('Digite o valor pago: R$ '))

if valor_pago < preco:
    print(f'Valor pago insuficiente. Você precisa pagar mais R$ {preco - valor_pago:.2f}')
elif valor_pago == preco:
    print('Pagamento realizado com sucesso. Sem troco.')
else:
    troco = valor_pago - preco
    print(f'Troco: R$ {troco:.2f}')

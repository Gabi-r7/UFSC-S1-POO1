valor_compra = float(input('Digite o valor da compra: R$ '))
percentual_desconto = 0.0

if valor_compra < 5000:
    percentual_desconto = 0.05
elif valor_compra >= 5000 and valor_compra < 7000:
    percentual_desconto = 0.15
elif valor_compra >= 7000:
    percentual_desconto = 0.25

valor_final = valor_compra - (percentual_desconto * valor_compra)

print(f'Valor da compra: R$ {valor_compra:.2f}\nPercentual de desconto: {percentual_desconto * 100}%\nValor final da compra: R$ {valor_final:.2f}')
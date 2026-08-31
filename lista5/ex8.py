num_dias, saldo_inicial = map(int, input('Digite o período de dias e o saldo inicial: ').split())
saldo_atual, menor_saldo = saldo_inicial, saldo_inicial

for i in range(1, num_dias+1):
    valor_movimentado = int(input(f'Digite o saldo do {i}° dia: '))

    saldo_atual += valor_movimentado

    if saldo_atual < menor_saldo:
        menor_saldo = saldo_atual

print(f'Menor saldo: {menor_saldo}')

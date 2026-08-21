salario = float(input('Digite o valor do salário: '))
percentual = 0

if salario > 0 and salario <= 400:
    percentual = 15
elif salario > 400 and salario <= 800:
    percentual = 12
elif salario > 800 and salario <= 1200:
    percentual = 10
elif salario > 1200 and salario <= 2000:
    percentual = 7
elif salario > 2000:
    percentual = 4
else:
    print('Erro no valor do salário')

novo_salario = salario + (salario * (percentual / 100))

print(f'Novo salário: {novo_salario:.2f}\nReajuste ganho: {novo_salario - salario:.2f}\nEm percentual: {percentual}%')

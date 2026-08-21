# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

nomeVendedor = input('Digite o nome do vendedor: ')
salarioFixo = float(input('Digite o salário fixo do vendedor: '))
totalVendas = float(input('Digite o total de vendas no mês (em dinheiro): '))

salarioFinal = salarioFixo + (totalVendas * 0.15)

print(f'O valor do salário com bônus é de R${salarioFinal:.2f}')
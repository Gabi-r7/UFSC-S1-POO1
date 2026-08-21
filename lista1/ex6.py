#Escreva um programa que leia o número de um funcionário,
#  seu número de horas trabalhadas, o valor que recebe por hora e calcula
#  o salário desse funcionário. A seguir, mostre o número e o salário
#  do funcionário, com duas casas decimais.

numeroFuncionario = int(input('Digite o número do funcionário: '))
horasTrabalhadas = float(input('Digite o número de horas trabalhadas: '))
salarioPorHora = float(input('Digite o valor recebido por hora: '))

salario = horasTrabalhadas * salarioPorHora

print(f'O funcionário número {numeroFuncionario} recebe R${salario:.2f}')
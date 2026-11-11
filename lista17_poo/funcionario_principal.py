'''
Exerc 01 - Aula 01 - Conceitos Classe

Implementar um programa que calcule o aumento de salário dos funcionários de uma empresa.
 O aumento está condicionado ao atual salário de cada funcionário.
Regras:
para abaixo ou igual a R$2.000,00 : aumento de 15%;
para 2.000,00 < salarioAtual < = 3.000,00: aumento de 10%;
para acima de 3.000,00: aumento igual a 5%.

Calcular o aumento de 3 funcionários;

A cada cálculo efetuado imprimir as seguintes informações:
nome do funcionário,
salário atual e
salário com reajuste. 

Devem ser implementadas 2 arquivos (.py):
Um arquivo contendo uma classe Funcionário que conterá os métodos para calcular
o aumento de salário e o construtor. 
Um arquivo contendo o controle_do_Funcionário (main), onde serão feitas chamadas
para criar instâncias da classe Funcionário e também acessar  os métodos que pertencem
a classe Funcionário.  
'''

from funcionario import Funcionario

f1 = Funcionario('Carla',5000)   # nome e salário atual
f2 = Funcionario('Ronaldo',2500)
f3 = Funcionario('Maria', 1500)

#exemplo 1
#invocando método sem passagem de parâmetro
f1.aumento_salarial2()

#exemplo2
#invocando o método com passagem de parâmetro
f2.aumento_salarial1(f2.salarioAtual)
f3.aumento_salarial1(f3.salarioAtual)

print('='*40)
f1.info_funcionario()
print('='*40)
f2.info_funcionario()
print('='*40)
f3.info_funcionario()
print('='*40)
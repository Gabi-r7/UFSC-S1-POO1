# Gabriel Henrique Lamb
# 26205861

quantMulheresSalario = 0
maiorSalario = 0
sexoPessoaMaiorSalario = 0
idadePessoaMaiorSalario = 0
menorIdade = 999
nomePessoaMaisNova = ''

while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').upper()
    salario = float(input('Digite o salário: '))

    if sexo == 'F' and salario < 2000:
        quantMulheresSalario += 1
    if salario > maiorSalario:
        maiorSalario = salario
        sexoPessoaMaiorSalario = sexo
        idadePessoaMaiorSalario = idade
    if idade < menorIdade:
        menorIdade = idade
        nomePessoaMaisNova = nome

    continuar = input('Deseja continuar cadastrando? (S/N): ').upper()
    if continuar == 'N':
        break

print(f'Quantidade de mulheres com salário < R$2.000,00: {quantMulheresSalario}')
print(f'Sexo e idade da pessoa com maior salário:\nSexo: {sexoPessoaMaiorSalario}, Idade: {idadePessoaMaiorSalario}')
print(f'Nome do morador mais novo: {nomePessoaMaisNova}')

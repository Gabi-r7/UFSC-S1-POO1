nome_melhor = ''
nota_melhor, mensalidade_melhor = 0, 0

for i in range(1, 6):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota geral do aluno: '))
    mensalidade = float(input('Digite o valor da mensalidade do aluno: '))

    if nota > nota_melhor:
        nome_melhor = nome
        nota_melhor = nota
        mensalidade_melhor = mensalidade

print(f'O aluno com a melhor nota foi:\nNome: {nome_melhor}\nNota: {nota_melhor}\nMensalidade sem desconto: R${mensalidade_melhor:.2f}\nMensalidade com desconto: R${mensalidade_melhor - (mensalidade_melhor * 0.3):.2f}')

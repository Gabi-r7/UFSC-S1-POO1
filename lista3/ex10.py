nome_melhor = ''
nota_melhor, media_turma = 0, 0

for i in range(1, 6):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota geral do aluno: '))
    media_turma += nota

    if nota > nota_melhor:
        nome_melhor = nome
        nota_melhor = nota

media_turma /= 5

if nota_melhor < 2.75:
    conceito = 'Reprovado'
elif nota_melhor > 2.75 and nota_melhor < 5.75:
    conceito = 'Em recuperação'
elif nota_melhor > 5.75:
    conceito = 'Aprovado'
else:
    print('Erro!')

print(f'A média da turma foi de {media_turma:.2f}\nO aluno com a melhor nota foi:\nNome: {nome_melhor}\nNota: {nota_melhor}\nConceito: {conceito}')

n = int(input())

alunos = {}
intrusos, epr, ehd = 0, 0, 0

for i in range(n):
    matricula, codigo = map(str, input().split())
    alunos.update({int(matricula): codigo})

for aluno in alunos:
    if alunos[aluno] == 'EPR':
        epr += 1
    elif alunos[aluno] == 'EHD':
        ehd += 1
    else:
        intrusos += 1

print(f'EPR: {epr}\nEHD: {ehd}\nINTRUSOS: {intrusos}')

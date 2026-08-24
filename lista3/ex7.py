n = int(input('Digite o número de pessoas a serem consultadas: '))
idades = 0

for i in range(n):
    idades += int(input('Digite sua idade: '))

media_idade = idades / n

if media_idade > 0 and media_idade < 25:
    print(f'A turma é jovem com idade média de {media_idade}')
elif media_idade > 25 and media_idade < 61:
    print(f'A turma é adulta com idade média de {media_idade}')
elif media_idade > 60:
    print(f'A turma é idosa com idade média de {media_idade}')
else:
    print('Erro!')
pessoas = list()

cont = 0
continuar = 0
mediaPesos = 0
while True:
    pessoa = list()
    if cont != 0:
        continuar = int(input('Deseja continuar? (1 para parar): '))
        if continuar == 1:
            break

    pessoa.append(input('Nome: '))
    pessoa.append(input('Idade: '))
    pessoa.append(input('Peso: '))

    mediaPesos += int(pessoa[2])
    
    pessoas.append(pessoa)

    cont += 1

mediaPesos /= cont
acimaDaMediaPeso = list()
abaixoDaMediaPeso = list()

print(f'Foram cadastradas {len(pessoas)} pessoas')

print('Mais de 20 anos: ')
maisDeVinte = 0
for i in range(len(pessoas)):
    aux = pessoas[i]
    if int(aux[1]) > 20:
        print(aux[0], aux[1])
        maisDeVinte += 1
    
    if int(aux[2]) > mediaPesos:
        acimaDaMediaPeso.append(aux[0])
    elif int(aux[2]) < mediaPesos:
        abaixoDaMediaPeso.append(aux[0])

print(f'{maisDeVinte} pessoa(s) com mais de vinte anos')

print(f'Pessoas mais pesadas: {acimaDaMediaPeso}')
print(f'Pessoas mais leves: {abaixoDaMediaPeso}')

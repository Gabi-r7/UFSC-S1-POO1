n1 = float(input('Digite o valor da nota 1: '))
n2 = float(input('Digite o valor da nota 2: '))
n3 = float(input('Digite o valor da nota 3: '))

media = (n1 + n2 + n3) / 3

if media < 5: 
    print(f'Reprovado com média {media:.2f}')
elif 7 > media > 5:
    print(f'Em recuperação com média {media:.2f}')
elif media > 7:
    print(f'Aprovado com média {media:.2f}')
else:
    print('Erro!')

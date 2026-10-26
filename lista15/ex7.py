x = int(input())

pessoas = {}

for i in range(x):
    nome, p1, p2, p3 = map(str, input().split())

    pessoas.update({nome: [p1, p2, p3]})

while True:
    nome, presente = map(str, input().split())

    if nome == 'parar':
        break

    certo = False

    for p in pessoas[nome]:        
        if p == presente:
            certo = True
            print('Uhul! Seu amigo secreto vai adorar o/')

    if not certo:
        print('Tente Novamente!')

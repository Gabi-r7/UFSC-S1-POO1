n = int(input())

traducoes = {}

for i in range(n):
    idioma = input()
    traducao = input()

    traducoes.update({idioma: traducao})

m = int(input())

for i in range(m):
    nome = input()
    auxIdioma = input()

    if traducoes.get(auxIdioma):
        print(nome)
        print(traducoes[auxIdioma])
    else:
        print('Idioma não encontrado')

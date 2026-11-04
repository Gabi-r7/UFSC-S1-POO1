x = int(input())

dic = {}

for i in range(x):
    livros = []
    livros.extend(input().split())
    dono = livros[0]
    livros = livros[1:]
    dic.update({dono: livros})

print('Consulta:')
continuar = 'S'

while continuar != 'N':
    nome, titulo = input().split()
    encontrado = False

    l = dic.get(nome)
    if l == None:
        print('Esta pessoa não está cadastrada.')
    else:
        for _ in l:
            if _ == titulo:
                print('Livro Encontrado!')
                encontrado = True
                break

        if not encontrado:
            print('Tente Novamente! Continue procurando com outro primo...')

    continuar = input('Deseja continuar: (S/N): ').upper()

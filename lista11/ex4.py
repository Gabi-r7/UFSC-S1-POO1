n = int(input('Digite o número de candidatos: '))

nomes = list()
requisitos = set()
aprovados = set()

for i in range(n):
    requisitos.clear()

    nomes.append(input('Digite o nome: '))

    requisitos.update(map(int, input('Digite as opçoes que você sabe: \n1 - Python\n2 - SQL\n3 - Javascript\n4 - C#\nSeus conhecimentos (separados por espaço): ').split()))

    if 1 in requisitos and 2 in requisitos and 3 in requisitos and 4 in requisitos:
        aprovados.add(nomes[i])

print(f'Candidatos aprovados: {aprovados}')

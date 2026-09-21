continuar = 'S'

while continuar != 'N':
    m = input().split()
    soma = 0

    for i in range(int(m[0])):
        soma += int(m[1][i])

    if soma % 3 == 0:
        print('Sim')
    else:
        print('Não')

    continuar = input('Deseja continuar? (S/N): ').upper()

print('Fim')

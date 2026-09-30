conjunto = set()
repetidos = []
n = int(input())

for i in range(n):
    aux = int(input())

    if aux in conjunto:
        repetidos.append(aux)
    else:
        conjunto.add(aux)

print(f'Set: {conjunto}')

if len(repetidos) > 0:
    print(f'Repetidos: {repetidos}')
else:
    print('Não houve números repetidos')

n = int(input())

seres = {}
maiorPoder = 0
ganhadores = []

for i in range(n):
    nome, poder = map(str, input().split())
    seres.update({nome: int(poder)})

    if int(poder) > maiorPoder:
        maiorPoder = int(poder)
        ganhador = nome

cont = 0

for _ in seres:
    if seres[_] == maiorPoder:
        cont += 1
        ganhadores.append(_)

if cont > 1:

        
    if len(sorted(ganhadores)[0]) < len(sorted(ganhadores)[1]):
        ganhador = sorted(ganhadores)[0]
    else:
        ganhador = f'{sorted(ganhadores)[0]}, {sorted(ganhadores)[1]}'
        
print(ganhador)
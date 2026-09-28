aposta = []
sorteados = []
aposta.extend(map(int, input().split()))
sorteados.extend(map(int, input().split()))
iguais = 0

for i in range(6):
    for j in range(6):
        if aposta[i] == sorteados[j]:
            iguais += 1

if iguais == 3:
    print('terno')
elif iguais == 4:
    print('quadra')
elif iguais == 5:
    print('quina')
elif iguais == 6:
    print('sena')
else:
    print('azar')

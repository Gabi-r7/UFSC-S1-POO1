p, n = map(int, input().split())
alturas = []
winner = True

alturas.extend(map(int, input().split()))

for i in range(len(alturas)):
    if i < len(alturas) - 1:
        if (alturas[i] - alturas[i + 1]) > p:
            winner = False
            break
    if i > 0:
        if (alturas[i] - alturas[i - 1]) > p:
            winner = False
            break

if winner:
    print('YOU WIN')
else:
    print('GAME OVER')

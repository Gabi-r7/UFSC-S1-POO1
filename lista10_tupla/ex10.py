n = int(input())
precos = []

precos.extend(map(int, input().split()))

for i in range(n):
    if precos[i] < 150:
        precos[i] += precos[i] * 0.15
        print(precos[i])
    elif precos[i] > 650:
        precos[i] -= precos[i] * 0.05
        print(precos[i])

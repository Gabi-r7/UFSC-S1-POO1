conjunto = set()

n = int(input())

for i in range(n-1):
    conjunto.add(int(input()))

for i in range(1, n):
    aux = i

    if i < len(conjunto)+1:
        if not(aux in conjunto):
            print('\n',aux)

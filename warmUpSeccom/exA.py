n = int(input())

for i in range(n):
    lista = list()

    lista.extend(map(int, input().split()))

    if lista[0] > 20 or lista[1] > 20 or lista[2] > 20:
        print(f'Case {i+1}: bad')
    else:
        print(f'Case {i+1}: good')

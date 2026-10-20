i = 0
while True:
    n = int(input())
    if n == 0:
        break

    i += 1
    lista = list()

    lista.extend(map(int, input().split()))

    done = 0

    for j in range(len(lista)):
        if lista[j] == 0:
            done += 1

    print(f'Case {i}: {len(lista) - (2 * done)}')

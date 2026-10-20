while True:
    a, b = map(int, input().split())

    if a == b == -1:
        break

    subindo = (b - a) % 100
    descendo = (a - b) % 100

    print(min(subindo, descendo))
    
while True:
    n = int(input())
    if n == 0:
        break

    rpms = []

    queda = 0

    rpms.extend(map(int, input().split()))
    aux = rpms[0]

    for i in range(len(rpms)):
        if i > 0:
            if rpms[i] < aux:
                queda = i + 1
                break
            aux = rpms[i]

    print(queda)

while True:
    m, n = map(int, input('Digite dois valores separados por espaço: ').split())
    sum = 0

    if m <= 0 or n <= 0:
        break

    if m > n:
        while True:
            if n > m:
                print(f'Sum={sum}')
                break

            print(n, ' ', end='')
            sum += n
            n += 1

    elif n > m:
        while True:
            if m > n:
                print(f'Sum={sum}')
                break

            print(m, ' ', end='')
            sum += m
            m += 1

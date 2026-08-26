n = 1

while n > 0:
    n = int(input('Digite quantos elementos da sequência você deseja ver: '))

    a, b = 0, 1
    i = 0
    while i < n:
        print(a, '-', end=' ')
        a, b = b, a + b
        i += 1
    
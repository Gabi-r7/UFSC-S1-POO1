a, b, c, d = map(int, input('Digite os valores de a, b, c e d: ').split())

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores não aceitos')

c, p, f = map(int, (input('Digite a quantidade de competidores, papel comprado, folhas por competidor: ').split()))

if p >= c * f:
    print('S')
else:
    print('N')

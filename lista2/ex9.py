a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b ** 2) - (4 * a * c)

if delta < 0 or 2 * a == 0:
    print('Impossível calcular')
else:
    x1 = (b * (-1) + (delta ** 0.5)) / (2 * a)
    x2 = (b * (-1) - (delta ** 0.5)) / (2 * a)

    print(f'R1: {x1:.5f}\nR2: {x2:.5f}')

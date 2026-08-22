a, b, c = map(float, input('Digite os lados do triângulo: ').split())

A, B, C = sorted((a, b, c), reverse=True)

if A < B + C:
    if A == B == C:
        print('Triângulo equilátero')
    elif A == B or B == C or A == C:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')

    if A**2 == B**2 + C**2:
        print('É um triângulo retângulo')
    elif A**2 > B**2 + C**2:
        print('É um triângulo obtusângulo')
    else:
        print('É um triângulo acutângulo')
else:
    print('Os valores não formam um triângulo')


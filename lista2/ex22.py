a, b, c = map(float, input('Digite os lados do triângulo: ').split())

A, B, C = sorted((a, b, c), reverse=True)

if A >= B + C:
    print('NAO FORMA TRIANGULO')
elif a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or a == c or b == c:
    print('TRIANGULO ISOSCELES')
else:
    if A ** 2 == B ** 2 + C ** 2:
        print('TRIANGULO RETANGULO')
    elif A ** 2 > B ** 2 + C ** 2:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')


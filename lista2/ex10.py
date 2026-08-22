a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
elif c > a and c > b:
    if a > b:
        print(a)
    else:
        print(b)
else:
    print('Erro!')
    
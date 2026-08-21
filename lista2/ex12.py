n1 = int(input('Digite o primeiro lado: '))
n2, n3, n4, n5 = map(int, input('Digite os próximos 4 lados (separado por espaço): ').split())
n6 = int(input('Digite o último lado: '))

if (n1 + n6 == 7) and (n2 + n4 == 7) and (n3 + n5 == 7):
    print('SIM')
else:
    print('NAO')

num = int(input('Digite um número: '))
divisiveis = 0

for i in range(num, 0, -1):
    if num % i == 0:
        divisiveis += 1
        print(f'{num} é divisível por {i}')

if divisiveis <= 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')

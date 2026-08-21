codigo, quantidade = map(int, input('Digite o código seguido da quantidade do item: ').split())
total = 0

if codigo == 1:
    total = quantidade * 4
elif codigo == 2:
    total = quantidade * 4.50
elif codigo == 3:
    total = quantidade * 5
elif codigo == 4:
    total = quantidade * 2
elif codigo == 5:
    total = quantidade * 1.5
else:
    print('Erro!')

print(f'Total: R${total:.2f}')

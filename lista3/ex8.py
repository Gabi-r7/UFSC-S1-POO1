n1 = int(input('Digite o número inicial: '))
n2 = int(input('Digite o número final: '))
soma = 0
produto = 1

if n1 > n2:
    print('Erro! Números inválidos')
else:
    for i in range(n1, n2 + 1):
        soma += i
        produto *= i

print(f'A soma e o produto dos números entre {n1} e {n2} é de:\nsoma: {soma}\nproduto: {produto}')

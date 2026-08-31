x = int(input('Digite o valor de x: '))

while True:
    z = int(input('Digite o valor de z: '))
    
    if z > x:
        break

soma = 0
contador = 0
valor = x

while soma <= z:
    soma += valor
    valor += 1
    contador += 1

print(f'Quantidade de números somados: {contador}')

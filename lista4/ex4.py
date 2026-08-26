n = int(input('Digite um valor: '))
aux = 0

while True:
    aux += 1

    if aux % n == 2:
        print(aux)

    if aux == 10000:
        break

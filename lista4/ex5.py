while True:
    num = int(input('Digite um número para verificar sua tabuada: '))
    aux = 1

    while aux <= 10:
        print(f'{aux} x {num} = {aux * num}')
        aux += 1

    continuar = int(input('Digite 1 para continuar ou outro número para parar: '))

    if continuar != 1:
        break

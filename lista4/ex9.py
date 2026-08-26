while True:
    x, y = map(int, input('Digite um par ordenado x e y: ').split())

    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    else:
        break

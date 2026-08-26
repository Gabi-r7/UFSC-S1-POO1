x = 1
while x != 0:
    x = int(input('\nDigite um número (0 para parar): '))
    aux = 1

    while aux <= x:
        print(aux, ' ', end='')
        aux += 1
    
    
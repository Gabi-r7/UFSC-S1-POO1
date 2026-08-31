rodadas = int(input('Digite a quantidade de rodadas: '))
sum_aldo, sum_beto = 0, 0
cont_rounds = 0
i = 1

while rodadas != 0:
    aldo, beto = map(int, input('Digite quantas cartas Aldo e Beto viraram, respectivamente: ').split())

    sum_aldo += aldo
    sum_beto += beto

    if i == rodadas:
        cont_rounds += 1
        print(f'Teste {cont_rounds}') 
        if sum_aldo > sum_beto:
            print('Aldo\n')
        else:
            print('Beto\n')

        rodadas = int(input('Digite a quantidade de rodadas: '))
        if rodadas == 0:
            break
        i = 0

    i += 1

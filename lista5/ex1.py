continuar = True

while continuar:
    ganhador = 0

    player1 = int(input('Jogador 1, Digite:\n0 - Encerrar o programa\n1 - Pedra\n2 - Papel\n3 - Tesoura\nSua escolha: '))
    player2 = int(input('Jogador 2, Digite:\n0 - Encerrar o programa\n1 - Pedra\n2 - Papel\n3 - Tesoura\nSua escolha: '))


    if player1 == 0 or player2 == 0:
        break
    elif player1 == 1:  #p1 -> pedra
        if player2 == 3:
            ganhador = 1
        elif player2 == 2:
            ganhador = 2
        
    elif player1 == 2:  #p1 -> papel
        if player2 == 1:
            ganhador = 1
        elif player2 == 3:
            ganhador = 2

    elif player1 == 3:  #p1 -> tesoura
        if player2 == 1:
            ganhador = 2
        elif player1 == 2:
            ganhador = 1

    else:
        print('\nEntrada inválida\n')

    if ganhador == 0:
        print('\nEmpate\n')
    elif ganhador == 1:
        print('\nJogador 1 ganhou\n')
    else:
        print('\nJogador 2 ganhou\n')

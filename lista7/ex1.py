while True:
    num_comandos = int(input('Digite o número de comandos: '))

    if num_comandos == 0:
        break

    lista_comandos = input().upper()
    virado_para = 'N'
    direcoes = ['N', 'L', 'S', 'O']

    quant_direita = lista_comandos.count('D')
    quant_esquerda = lista_comandos.count('E')

    acoes = quant_direita - quant_esquerda
    posicao = acoes % 4

    print(direcoes[posicao])

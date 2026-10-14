while True:
    nQuestoes = int(input())
    
    if nQuestoes == 0:
        break

    alternativas = ['A', 'B', 'C', 'D', 'E']

    for i in range(nQuestoes):
        lista = list()
        marcada = 'nada'
        lista.extend(map(int, input().split()))

        for i in range(len(lista)):
            if lista[i] <= 127:
                if marcada == 'nada':
                    marcada = alternativas[i]
                else:
                    marcada = '*'
                    break

        print(marcada)

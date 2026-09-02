
def verifica_entrada(a, b, aux): #(1 ≤ N ≤ 1000 e 1 ≤ C ≤ 1000) , (0 ≤ S ≤ 1000 e 0 ≤ E ≤ 1000)
    if aux <= a <= 1000 and aux <= b <= 1000:
        return True
    else:
        return False

def controle_capacidade():
    entrada_valida = False
    total_pessoas = 0
    capacidade_excedida = False

    while not entrada_valida:
        leituras, capacidade_maxima = map(int, input('Digite o número de leituras realizadas e a capacidade máxima: ').split())

        entrada_valida = verifica_entrada(leituras, capacidade_maxima, 1)


    for i in range(leituras):
        entrada_valida = False

        while not entrada_valida:
            saidas, entradas = map(int, input('Digite a quantidade de saídas e entradas: ').split())
            entrada_valida = verifica_entrada(saidas, entradas, 0)

        total_pessoas -= saidas
        total_pessoas += entradas

        if total_pessoas > capacidade_maxima:
            capacidade_excedida = True

    if capacidade_excedida:
        print('S')
    else:
        print('N')

controle_capacidade()

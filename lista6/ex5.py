
def main():
    entrada_valida = False
    colchao_passa = saida(entrada_valida)

    if colchao_passa:
        print('Parabéns, esse colchão passa na porta!')
    else:
        print('Infelizmente esse colchão não passa na porta. Procure outro!')

def verifica_entrada(a, b, c, aux1, h, l, aux2):
    if 1 <= a <= aux1 and 1 <= b <= aux1 and 1 <= c <= aux1 and 1 <= h <= aux2 and 1 <= l <= aux2:
        return True
    else:
        return False

def saida(entrada_valida):
    while not entrada_valida:
        a, b, c = map(int, input('Digite as medidas do colchão (em cm): ').split())
        h, l = map(int, input('Digite as medidas da porta (altura x largura, em cm): ').split())
        entrada_valida = verifica_entrada(a, b, c, 300, h, l, 250)

    if (a <= h and b <= l) or (a <= l and b <= h) or (a <= h and c <= l) or (a <= l and c <= h) or (b <= h and c <= l) or (b <= l and c <= h):
        return True
    else:
        return False

main()

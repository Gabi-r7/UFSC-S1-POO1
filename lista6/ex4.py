entrada_valida = False

def verifica_entrada(s, t, f): #S (0 ≤ S ≤ 23), T (1 ≤ T ≤ 12) e F (-5 ≤ F ≤ 5)
    if 0 <= s <= 23 or 1 <= t <= 12 or -5 <= f <= 5:
        return True
    else:
        return False

def fuso(s, t, f):

    if s == 0:
        s = 24

    hora_destino = s + t + f

    if hora_destino > 24:
        hora_destino = hora_destino % 24
    elif hora_destino == 24:
        hora_destino = 0

    print(hora_destino)


while not entrada_valida:
    s, t, f = map(int, input('Digite a hora da saída, tempo de viagem e o fuso de destino: ').split())
    entrada_valida = verifica_entrada(s, t, f)    

fuso(s, t, f)
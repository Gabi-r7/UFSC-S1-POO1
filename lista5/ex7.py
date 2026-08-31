d, vf, vg = map(float, input('Digite a distância, velocidade fugitivo e velocidade guarda: ').split())
limite = 12  
dg = (d**2 + limite**2)**0.5

if vg <= vf:
    print('N')
else:
    tempof = 12 / vf
    tempog = dg / vg

    if tempog <= tempof:
        print('S')
    else:
        print('N')

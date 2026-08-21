cv, ce, cs, fv, fe, fs = map(int, (input('Digite os dados: ')).split())

pontos_c = cv * 3 + ce
pontos_f = fv * 3 + fe

if pontos_c > pontos_f:
    print('C')
elif pontos_f > pontos_c:
    print('F')
else:
    if cs > fs:
        print('C')
    elif fs > cs:
        print('F')
    else:
        print('=')

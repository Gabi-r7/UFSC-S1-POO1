a, b, c = map(int, input('Digite as medidas do colchão (em cm): ').split())
h, l = map(int, input('Digite as medidas da porta (altura x largura, em cm): ').split())
#a, b, c = sorted([a, b, c])

#duas medidas do colchão precisam ser menores ou iguais da porta

if (a <= h and b <= l) or (a <= l and b <= h) or (a <= h and c <= l) or (a <= l and c <= h) or (b <= h and c <= l) or (b <= l and c <= h):
    print('O colchão passa pela porta.')
else:
    print('O colchão não passa pela porta.')

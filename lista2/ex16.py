diametro_bola = int(input('Digite o diâmetro da bolda de boliche: '))
altura_caixa, largura_caixa, profundidade_caixa = map(int, (input('Digite a altura, largura e profundidade da caixa (separado por espaços):').split()))

if altura_caixa >= diametro_bola and largura_caixa >= diametro_bola and profundidade_caixa >= diametro_bola:
    print('S')
else:
    print('N')

# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

xPontoUm = float(input('Digite a coordenada x do ponto 1: '))
yPontoUm = float(input('Digite a coordenada y do ponto 1: '))
xPontoDois = float(input('Digite a coordenada x do ponto 2: '))
yPontoDois = float(input('Digite a coordenada y do ponto 2: '))

distancia = (((xPontoDois - xPontoUm) ** 2) + (yPontoDois - yPontoUm) ** 2) ** 0.5

print(f'A distância entre os dois pontos é de {distancia:.4f}')

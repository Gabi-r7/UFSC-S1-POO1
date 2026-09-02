largura = float(input('Digite o valor da largura do terreno: '))
comprimento = float(input('Digite o valor do comprimento do terreno: '))

def calcula_area(largura, comprimento):
    area = largura * comprimento

    print(f'A área do terreno é de {area:.2f}m²')


calcula_area(largura, comprimento)

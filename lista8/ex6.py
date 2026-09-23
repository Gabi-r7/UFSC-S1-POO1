def calc_media_e_retira_extremidades(lista):
    quant_numeros = len(lista)
    maior, menor, media = 0, 0, 0

    for i in range(quant_numeros):
        media += lista[i]

        if i == 0:
            maior = lista[i]
            menor = lista[i]
        
        elif lista[i] > maior:
            maior = lista[i]
        
        elif lista[i] < menor:
            menor = lista[i]

    lista.remove(maior)
    lista.remove(menor)
    media -= maior + menor
    media /= 3

    return maior, menor, media
        
def main():
    while True:
        nome = input('Atleta: ').upper()

        if nome == 'O':
            break

        lista = []

        for i in range(5):
            lista.append(float(input(f'{i}° salto: ')))
        
        maior, menor, media = calc_media_e_retira_extremidades(lista)
        
        print(f'Melhor salto: {maior:.1f}m\nPior salto: {menor:.1f}m\nMédia dos demais saltos: {media:.1f}m')
main()

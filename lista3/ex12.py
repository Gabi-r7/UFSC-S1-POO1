num_praias = int(input('Digite o número de praias: '))
distancia_media, praias_entre_15_e_20_kms, distancia_praia_mais_distante = 0, 0, 0
nome_praia_mais_distante = ''

for i in range(num_praias):
    nome_praia = input('Digite o nome da praia: ')
    distancia = float(input('Digite a distância do centro (em metros): '))
    distancia_media += distancia

    if distancia > distancia_praia_mais_distante:
        distancia_praia_mais_distante = distancia
        nome_praia_mais_distante = nome_praia
    if distancia >= 15000 and distancia <= 20000:
        praias_entre_15_e_20_kms += 1

distancia_media = round(distancia_media / num_praias, 1)

print(f'Praia mais distante: {nome_praia_mais_distante}, distância: {distancia_praia_mais_distante}\nPraias entre 15 e 20 kms do centro: {praias_entre_15_e_20_kms}\nDistância média das praias {distancia_media} Kms')

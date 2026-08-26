n = 0
alcool, gasolina, diesel = 0, 0, 0

while n != 4:
    n = int(input('Qual combustível você escolheu: \n1 - Álcool\n2 - Gasolina\n3 - Diesel\n4 - Fim\nDigite: '))

    if n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1

print(f'\nMUITO OBRIGADO\nÁlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')

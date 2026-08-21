peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Abaixo do peso ideal com IMC de {imc:.1f}')
elif imc > 18.5 and imc <= 25:
    print(f'Peso ideal com IMC de {imc:.1f}')
elif imc > 25 and imc <= 30:
    print(f'Sobrepeso com IMC de {imc:.1f}')
elif imc > 30 and imc <= 40:
    print(f'Obesidade com IMC de {imc:.1f}')
elif imc > 40:
    print(f'Obesidade mórbida com IMC de {imc:.1f}')
else:
    print('Erro no cálculo!')

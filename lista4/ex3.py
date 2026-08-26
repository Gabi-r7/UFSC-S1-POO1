
while True:
    salario = float(input('Digite o salário: '))

    porcentagem_desconto = 11
    desconto_calculado = salario * (porcentagem_desconto / 100)

    if desconto_calculado > 320:
        desconto_calculado = 320
        porcentagem_desconto = (320 / salario) * 100

    novo_salario = salario - desconto_calculado

    print(f'Seu novo salário é de R${novo_salario:.2f}\nPercentual de desconto: {porcentagem_desconto}%')

    parar = int(input('Digite 1 se deseja continuar ou outro valor parar: '))

    if parar != 1:
        break

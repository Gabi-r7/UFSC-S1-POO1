renda = float(input('Digite o valor da renda em R$: '))

if renda <= 2000:
    imposto_renda = 0.0
elif renda <= 3000:
    imposto_renda = (renda - 2000) * 0.08
elif renda <= 4500:
    imposto_renda = (renda - 3000) * 0.18 + 1000 * 0.08
else:
    imposto_renda = (renda - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08

print(f'O imposto devido é de R$ {imposto_renda:.2f}')
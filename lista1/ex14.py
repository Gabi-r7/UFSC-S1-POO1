# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

distanciaTotalPercorrida = int(input('Digite a distância total percorrida (em Km): '))
totalCombustivelGasto = float(input('Digite quantos litros de combustível foram gastos: '))

consumoMedio = distanciaTotalPercorrida / totalCombustivelGasto

print(f'O consumo médio de combustível é de: {consumoMedio:.3f} km/l')
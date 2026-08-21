# Escreva um programa que, dada a pressão desejada digitada pelo motorista e a pressão do pneu lida pela bomba, indica a diferença entre a pressão desejada e a pressão lida.
pressaoDesejada = float(input('Digite a pressão desejada: '))
pressaoLida = float(input('Digite a pressão lida: '))

diferenca = pressaoDesejada - pressaoLida

print(f'A diferença de pressão é de {diferenca}')
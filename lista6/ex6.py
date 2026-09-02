def main():
    pares, impares = 0, 0

    for i in range(1, 11):
        n = int(input(f'Digite o {i}° valor: '))
        par = e_par(n)

        if par:
            pares += 1
        else:
            impares += 1

    print(f'O total de números pares é: {pares}\nO total de números ímpares é: {impares}')

def e_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

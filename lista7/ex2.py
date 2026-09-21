n = int(input('Número de casos de teste: '))

for i in range(n):
    string = input()
    letra = string[1]
    n1 = int(string[0])
    n2 = int(string[2])

    if n1 == n2:
        resultado = n1 * n2
    elif letra.isupper():
        resultado = n2 - n1
    else:
        resultado = n1 + n2

    print(resultado)

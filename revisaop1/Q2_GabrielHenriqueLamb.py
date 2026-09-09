# Gabriel Henrique Lamb
# 26205861

def verificaPrimo(n):
    divisiveis = 0
    for i in range(n, 1, -1):
        if n % i == 0:
            divisiveis += 1

    if divisiveis == 2:
        return 1
    else:
        return 0

def verificaPar(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

def verificaPositivo(n):
    if n > 0:
        return 1
    else:
        return 0

def main():
    quantidade = int(input('Digite a quantidade de números: '))
    positivos = 0

    while positivos <= 0:
        positivos = 0
        primos = 0
        pares = 0
        media = 0
        quantidade_positivos = 0

        for i in range(1, quantidade + 1):
            n = int(input(f'Digite o valor para a {i}° posição: '))

            pares += verificaPar(n)
            positivos += verificaPositivo(n)

            if n > 0:
                media += n
                primos += verificaPrimo(n)
                quantidade_positivos += 1

        if positivos > 0:
            media /= quantidade_positivos
            print(f'{positivos} valor(es) positivo(s)\n{primos} número(s) primo(s)\n{pares} número(s) pare(s)\nMédia dos positivos: {media:.2f}')
        else:
            print('Ao menos um número deve ser positivo!')
main()

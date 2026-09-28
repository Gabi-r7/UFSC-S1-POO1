n = int(input())
lista = []
m2, m3, m4, m5 = 0, 0, 0, 0

lista.extend(map(int, input().split()))

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        m2 += 1
    if lista[i] % 3 == 0:
        m3 += 1
    if lista[i] % 4 == 0:
        m4 += 1
    if lista[i] % 5 == 0:
        m5 += 1

print(f'{m2} Multiplo(s) de 2')
print(f'{m3} Multiplo(s) de 3')
print(f'{m4} Multiplo(s) de 4')
print(f'{m5} Multiplo(s) de 5')

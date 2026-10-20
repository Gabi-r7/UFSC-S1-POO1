n = int(input())

for i in range(n):
    lista = list()

    lista.extend(map(int, input().split()))
       
    print(f'Case {i + 1}: {sorted(lista)[1]}')

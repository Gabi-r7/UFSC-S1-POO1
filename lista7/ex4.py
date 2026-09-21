n = int(input('casos teste: '))
tot_cobaias, tot_coelhos, tot_ratos, tot_sapos = 0, 0, 0, 0

for i in range(n):
    string = input().split()

    tot_cobaias += int(string[0])

    if string[1] == 'C':
        tot_coelhos += int(string[0])
    elif string[1] == 'R':
        tot_ratos += int(string[0])
    else:
        tot_sapos += int(string[0])

print(f'Total: {tot_cobaias} cobaias')
print(f'Total de coelhos: {tot_coelhos}')
print(f'Total de ratos: {tot_ratos}')
print(f'Total de sapos: {tot_sapos}')
print(f'Percentual de coelhos: {(tot_coelhos / tot_cobaias) * 100:.2f}%')
print(f'Percentual de ratos: {(tot_ratos / tot_cobaias) * 100:.2f}%')
print(f'Percentual de sapos: {(tot_sapos / tot_cobaias) * 100:.2f}%')

num_celulas = int(input('Digite o número de células: '))

bombas = list()
nums = list()

for i in range(num_celulas):
    bombas.append(int(input()))
    nums.append(0)

for i in range(len(bombas)):

    if bombas[i] == 1:
        nums[i] += 1
        if i > 0:
            nums[i-1] += 1
        if i < len(bombas) - 1:
            nums[i+1] += 1

print(nums)

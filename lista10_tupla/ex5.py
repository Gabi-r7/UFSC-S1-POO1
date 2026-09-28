x = []
y = []

x.extend(map(int, input().split()))
y.extend(map(int, input().split()))

for i in range(5):
    if x[i] + y[i] > 1:
        print('N')
        break
    if i == 4:
        print('Y')

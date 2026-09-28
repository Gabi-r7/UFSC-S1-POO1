n, r = map(int, input().split())
voltaram = []
morreram = []

voltaram.extend(map(int, input().split()))

for i in range(1, n):
    if i not in voltaram:
        morreram.append(i)

if len(morreram) < 1:
    print('*')
else:
    for i in morreram:
        print(i, end=' ')

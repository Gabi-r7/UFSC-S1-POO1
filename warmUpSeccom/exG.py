n = int(input())

print('Lumberjacks:')

for _ in range(n):
    order = list(map(int, input().split()))

    if order == sorted(order) or order == sorted(order, reverse=True):
        print('Ordered')
    else:
        print('Unordered')
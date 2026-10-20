n = int(input())
approved = 0

for i in range(n):
    length, width, depth, weight = map(float, input().split())

    valid_dimensions = (
        (length <= 56 and width <= 45 and depth <= 25)
        or length + width + depth <= 125
    )

    if valid_dimensions and weight <= 7:
        print(1)
        approved += 1
    else:
        print(0)
    
print(approved)

n = int(input())

data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(n):
    over = 1
    for j in range(n):
        if i == j:
            continue
        else:
            if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
                over += 1
    print(over, end=' ')


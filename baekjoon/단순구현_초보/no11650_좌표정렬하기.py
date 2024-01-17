n = int(input())

data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort(key=lambda x: (x[0], x[1]))

for tup in data:
    print(*tup)
h, w = map(int, input().split())

graph = [[0] * w for _ in range(h)]

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for l, d, x, y in data:
    x -= 1
    y -= 1
    if d == 1:
        for _ in range(l):
            if x >= h:
                continue
            graph[x][y] = 1
            x += 1

    else:
        for _ in range(l):
            if y >= w:
                continue
            graph[x][y] = 1
            y += 1


for line in graph:
    print(*line)
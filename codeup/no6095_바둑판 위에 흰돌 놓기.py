n = int(input())

graph = [[0] * 19 for _ in range(19)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for line in graph:
    print(*line)

import sys
input = sys.stdin.readline

flip = {}
flip[0] = 1
flip[1] = 0

graph = []
for _ in range(19):
    line = list(map(int, input().split()))
    graph.append(line)

n = int(input())

direction = []
for _ in range(n):
    a, b = map(int, input().split())
    direction.append((a - 1, b - 1)) # 인덱스 값과 맞추기 위해 -1

for a, b in direction:
    for col in range(len(graph[0])):
        graph[a][col] = flip.get(graph[a][col])

for a, b in direction:
    for row in range(len(graph)):
        graph[row][b] = flip.get(graph[row][b])


for line in graph:
    print(*line)
# 미로 상 하 좌 우 보면서 1일경우 + 1만 해주면서 전진
# 1인 애들만 큐에 넣고, 뺀 후에
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    line = input()
    graph.append([int(s) for s in line])

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))



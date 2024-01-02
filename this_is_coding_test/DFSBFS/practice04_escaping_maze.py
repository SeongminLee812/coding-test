from collections import deque
from pprint import pprint

# input n, m
n, m = map(int, input().split())

# map information 2d list
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# define direction to move (up, down, left, right)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# implement bfs
def bfs(x, y):
    # queue
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        pprint(graph)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # continue if out of range
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # continue if monster
            if graph[nx][ny] == 0:
                continue
            # record shortest path only first visit
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
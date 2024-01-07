from collections import deque
n, m = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
x, y = 0, 0

q = deque([(x, y)])

while q:
    x, y = q.popleft()
    visited[x][y] = True
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] != 0 and not visited[nx][ny]:
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])
print(graph)






"""
test case

5 6
101010
111111
000001
111111
111111

"""


# =======================교재 답안========================
from collections import deque

# # n, m을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
#
# # 2차원 리스트의 맵 정보 입력받기
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))

# 이동할 네 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 구현
def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어나는 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    # 최단거리 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))
print(graph)

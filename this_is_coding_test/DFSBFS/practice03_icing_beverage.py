import sys
from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 해당노드 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        # 상하좌우 모두 재귀적으로 호출 -> 연결되어 있는 노드는 다 1로 바꿔버린다
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)

n, m = map(int, input().split())

def dfs(graph, i, j):
    if i >= n or i < 0 or j >= m or j < 0:
        return False

    if graph[i][j] == 1:
        return False
    else:
        graph[i][j] = 1
        dfs(graph, i - 1, j)
        dfs(graph, i + 1, j)
        dfs(graph, i, j - 1)
        dfs(graph, i, j + 1)
    return True

graph = []

for _ in range(n):
    data = input()
    graph.append([int(s) for s in data])

count = 0
# 완전탐색
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):
            count += 1

print(count)
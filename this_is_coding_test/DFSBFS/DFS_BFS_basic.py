import sys
from collections import deque
INF = sys.maxsize

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# node 1
graph[1].append((0, 7))

# node2
graph[2].append((0, 5))

print(graph)

search_list = []
# define DFS method
def dfs(graph, v, visited):
    # check visit current node
    visited[v] = True
    print(v, end=' ')
    # recursively visit another node which connected
    for i in graph[v]:
        if not visited[i]:
            print(f'{v} 노드에서 {i} 노드 탐색')
            dfs(graph, i, visited)
    print(f'{v} 노드 재귀함수 종료')

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 1d-list to represent visit information
visited = [False] * 9

dfs(graph, 1, visited)


# bfs method
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 1d-list to represent visit information
visited = [False] * 9

bfs(graph, 1, visited)
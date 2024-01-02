def dfs(graph, v, visited):
    # check visit current node
    visited[v] = True
    print(v, end=' ')
    # recursively visit another node which is connected
    for i in graph[v]:
        # search only not visited
        if not visited[i]:
            dfs(graph, i, visited)

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
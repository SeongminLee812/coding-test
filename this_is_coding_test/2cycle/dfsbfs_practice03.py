n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    if graph[i][j] == 0:
        graph[i][j] = 1
        # 상하좌우 재귀적으로 호출
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)


"""
test case

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

4 5
00110
00011
11111
00000
"""
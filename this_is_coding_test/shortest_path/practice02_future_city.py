# 내 풀이 -> 다익스트라 2번
"""
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    if distance[end] == INF:
        return INF
    return distance[end]


to_k = dijkstra(1, k)
distance = [INF] * (n + 1)
to_x = dijkstra(k, x)

result = to_k + to_x
if result >= INF:
    print(-1)
else:
    print(result)
"""

# test case
"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""

# 교재 풀이
INF = int(1e9) # 무한 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# for i in range(1, n + 1):
#     graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 x와 최종 목적지 k
x, k = map(int, input().split())

# 점화식에 따라 플루이드 워셜 알고리즘 수행
for j in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][j] + graph[j][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)
import sys
import heapq
from collections import deque

input = sys.stdin.readline

# n, m, k, x = map(int, input().split()
# graph = [[] for _ in range(n + 1)]
# INF = int(1e9)
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append((b, 1))
#
# def dijstra(start):
#     q = []
#     heapq.heappush(q, (0, start)) # 비용과 최단거리 다 넣기
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#         if dist > distance[now]: # 처리된 적이 있으면 통과
#             continue
#
#         for i in graph[now]: # 연결된 노드 확인
#             cost = distance[now] + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijstra(x)
#
# result = []
# for i in range(1, len(distance)):
#     if distance[i] == k:
#         result.append(i)
#
# if result:
#     for i in result:l
#         print(i)
# else:
#     print(-1)
#

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start):
    q = deque([start])
    distance = [-1] * (n + 1)
    distance[start] = 0

    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    return distance

distance = bfs(graph, x)

check = False
for i in distance:
    if i == k:
        print(i)
        check = True

if not check:
    print(-1)


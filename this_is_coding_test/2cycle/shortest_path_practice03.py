import sys
import heapq

input = sys.stdin.readline
v, e, start = map(int, input().split())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (v + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # i[0]이 노드 이름, i[1]이 비용
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for i in distance:
    if i != INF:
        count += 1
        max_distance = max(max_distance, i)

print(count - 1, max_distance)
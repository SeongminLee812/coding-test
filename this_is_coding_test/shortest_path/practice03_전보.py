import sys
import heapq
input = sys.stdin.readline

n, m, start = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(graph)
print(distance)
connected = [True for dist in distance if dist != INF and dist != 0]
total = [dist for dist in distance if dist != INF and dist != 0]

print(sum(connected), max(total))
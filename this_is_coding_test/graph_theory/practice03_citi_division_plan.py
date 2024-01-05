def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

result = 0
edge = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for cost, a, b in edge:
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        result += (cost)
        last = cost

print(result - last)



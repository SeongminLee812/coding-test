
v, e = map(int, input().split())

parent = [0] * (v + 1)

for i in range(0, v + 1):
    parent[i] = i

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

result = []
for _ in range(e):
    func, a, b = map(int, input().split())
    result.append((func, a, b))

for func, a, b, in result:
    if func == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')


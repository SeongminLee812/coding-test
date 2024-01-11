n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

results = []

for i in range(n):
    if data[i] >= m:
        continue
    for j in range(i + 1, n):
        if data[i] + data[j] >= m:
            continue
        for k in range(j + 1, n):
            if data[i] + data[j] + data[k] <= m:
                results.append(data[i] + data[j] + data[k])

print(max(results))


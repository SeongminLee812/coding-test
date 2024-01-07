results = []

n = int(input())
for _ in range(n):
    results.append(int(input()))

print(sorted(results, reverse=True))
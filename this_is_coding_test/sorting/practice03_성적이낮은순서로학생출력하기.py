n = int(input())

result = []
for _ in range(n):
    name, score = input().split()
    result.append((name, int(score)))

result = sorted(result, key = lambda x: x[1])

for name, score in result:
    print(name, end=' ')

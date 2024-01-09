a, m, d, n = map(int, input().split())

result = a

for _ in range(1, n):
    result = result * m + d

print(result)
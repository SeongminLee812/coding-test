
n, m = map(int, input().split())

balls = list(map(int, input().split()))

# brute force
"""
result = 0
for i in range(n):
    for j in range(i + 1, n):
        if balls[i] == balls[j]:
            continue
        result += 1


print(result)
"""

array = [0] * 11

for x in balls:
    array[x] += 1

result = 0
for i in range(1, n + 1):
    n -= array[i]
    result += array[i] * n
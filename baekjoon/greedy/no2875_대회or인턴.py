n, m, k = map(int, input().split())


result = 0

rest = n + m
while n >= 0 and m >= 0 and rest >= k:
    n -= 2
    m -= 1
    rest -= 3
    if rest < k or n < 0 or m < 0:
        continue
    result += 1

print(result)

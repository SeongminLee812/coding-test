n = int(input())

result = 0
for i in range(n):
    now = i
    for s in str(i):
        now += int(s)
    if now == n:
        result = i
        break

print(result)
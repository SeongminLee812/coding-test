n, m = map(int, input().split())

currency = []
for _ in range(n):
    currency.append(int(input()))

d = [10001] * 10001
d[0] = 0

for i in range(1, m + 1):
    for j in currency:
         d[i] = min(d[i], d[i - j] + 1)

if d[m] > 10000:
    print(-1)
else:
    print(d[m])


# 교재 답안
d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(currency[i], m + 1):
        d[j] = min(d[j], d[j - currency[i]] + 1)

print(d)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
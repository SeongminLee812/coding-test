n = int(input())

array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]
d[1] = array[1]

for i in range(2, len(array)):
    d[i] = max(d[:i - 1]) + array[i]

print(d)
print(max(d))

# 교재 답안
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d)
print(d[n - 1])
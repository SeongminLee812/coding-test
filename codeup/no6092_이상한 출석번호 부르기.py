n = int(input())
array = list(map(int, input().split()))

d = [0] * 23

for i in array:
    d[i - 1] += 1

print(*d)
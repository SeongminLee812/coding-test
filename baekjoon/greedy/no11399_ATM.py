n = int(input())
data = list(map(int, input().split()))

result = 0
data.sort()

time = 0
for i in data:
    time += i
    result += time

print(result)
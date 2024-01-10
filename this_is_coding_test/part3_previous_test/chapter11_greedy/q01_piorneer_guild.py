import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
count = 0

for d in data:
    count += 1
    if d <= count:
        result += 1
        count = 0

print(result)
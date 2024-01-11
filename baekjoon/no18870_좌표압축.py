import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

res = list(set(array))
res.sort()

result_dict = {}

for i in range(len(res)):
    result_dict[res[i]] = i

for d in array:
    print(result_dict[d], end=' ')


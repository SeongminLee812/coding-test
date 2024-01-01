import sys
#
n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# data.sort()
# group_count = 0
#
# group = []
#
# for i in data:
#     group.append(i)
#     if len(group) >= i:
#         group_count += 1
#         group = []
#     else:
#         continue
#
# print(group_count)
#

result = 0
count_in_group = 0

for i in data:
    count_in_group += 1
    if count_in_group >= i:
        count_in_group = 0
        result += 1

print(result)


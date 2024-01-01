import sys

"""
내 코드
N, M = map(int, input().split())

card_list = []
min_list = []
for _ in range(N):
    input_row = sys.stdin.readline().rstrip().split()
    row = list(map(int, input_row))
    min_list.append(min(row))
    card_list.append(row)

print(max(min_list))
"""

# # 교재 코드
# N, M = map(int, input().split())
#
# result = 0
# for _ in range(N):
#     input_row = list(map(int, sys.stdin.readline().rstrip().split()))
#     min_value = min(input_row)
#     result = max(result, min_value)
#
# print(result)

# 이중 반복문

n, m = map(int, input().split())
result = 0

for _ in range(n):
    input_row = list(map(int, sys.stdin.readline().rstrip().split()))
    min_value = sys.maxsize
    for i in input_row:
        min_value = min(min_value, i)
    result = max(result, min_value)

print(result)
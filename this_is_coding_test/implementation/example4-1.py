# import sys
# import pprint
# N = int(input())
# data = sys.stdin.readline().rstrip().split()
#
# result = ""
# xy = [[(i, j) for j in range(1, N + 1)] for i in range(1, N + 1)]
#
# row = 0
# col = 0
#
# for direction in data:
#     if direction == 'R' and col < N:
#         col += 1
#     elif direction == 'U' and row > 0:
#         row -= 1
#     elif direction == 'L' and col > 0:
#         col -= 1
#     elif direction == 'D' and row < N:
#         row += 1
#     else:
#         pass
#
# print(xy[row][col][0], xy[row][col][1])
#

# 교재 답안
n = int(input())
a, b = 1, 1
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
da = [0, 0, -1, 1]
db = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            na = a + da[i]
            nb = b + db[i]
    if na < 1 or nb < 1 or na > n or nb > n:
        continue
    a, b = na, nb

print(a, b)


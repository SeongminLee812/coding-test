data = input()
point1, point2 = data[0], data[1]


point_dict = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [i for i in range(1, 9)]))
point1 = point_dict[point1]
point2 = int(point2)

move_row = [-2, -2, +2, +2, -1, +1, -1, +1]
move_col = [+1, -1, +1, -1, -2, -2, +2, +2]

count = 0

for i in range(8):
    d_row = point2 + move_row[i]
    d_col = point1 + move_col[i]
    if d_row < 1 or d_row > 8 or d_col < 1 or d_col > 8:
        continue
    count += 1

print(count)

# 교재 답안

# 현재 나이트의 위치
input_data = input()
row = int(input_data[1])
columns = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (1, 2), (2, 1), (2, -1), (-1, 2), (-2, 1)]

# 8가지 방향 전부 검사
result = 0
for step in steps:
    next_row = row + step[0]
    next_col = columns + step[1]
    if next_row < 1 or next_row > 8 or next_col < 1 or next_col > 8:
        continue
    result +=1


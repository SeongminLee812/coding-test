# n, m = map(int, input().split())
# x, y, dir_idx = map(int, input().split())
#
# graph = []
#
# for _ in range(n):
#     one_row = list(map(int, input().split()))
#     graph.append(one_row)
#
# direction = [0, 1, 2, 3]
# steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]
#
# def turn_left():
#     global dir_idx
#     dir_idx -= 1
#     if dir_idx == -1:
#         dir_idx = 3
#
# result = 1
# turn_times = 0
# while True:
#     graph[x][y] = 1
#     nx = x + steps[dir_idx][0]
#     ny = y + steps[dir_idx][1]
#     if graph[nx][ny] == 0:
#         x, y = nx, ny
#         result += 1
#         turn_left()
#         turn_times = 0
#     else:
#         turn_left()
#         turn_times += 1
#         if turn_times == 4:
#             if dir_idx == 0:
#                 nx = x + 1
#                 ny = y
#             elif dir_idx == 1:
#                 nx = x
#                 ny = y + 1
#             elif dir_idx == 2:
#                 nx = x - 1
#                 ny = y
#             else:
#                 nx = x
#                 ny = y - 1
#             if graph[nx][ny] == 1:
#                 break
#             else:
#                 x, y = nx, ny
#                 result += 1
#
# print(graph)
# print(result)
#


# 교재 답안

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 x, y 좌표, 방향
x, y, direction = map(int, input().split())
d[x][y] = 1

# 전체 맵 정보를 입력받기
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 바다이거나 가본 칸 인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)


"""
test case

4 4 
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
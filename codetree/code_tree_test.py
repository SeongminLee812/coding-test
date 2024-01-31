n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문한지 체크
c = [[False] * n for _ in range(n)]

def check(x, y):
    ok = True # 전부 체크된 걸 default
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= 0 or nx >= n or ny <= 0 or ny >= n:
            continue
        if c[nx][ny] != True and a[nx][ny] != 0:
            ok = False
    return ok


def dfs(x, y, count):
    global total
    if check(x, y):
        if count == 3:
            total += 1
        return

    if c[x][y]: # 이미 방문한 경우 종료
        return

    c[x][y] = True # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= 0 or nx >= n or ny <= 0 or ny >= n:
            continue
        dfs(nx, ny, count + 1)

total = 0

for i in range(n):
    for j in range(n):
        dfs(i, j, 0)

print(total)
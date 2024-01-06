n = int(input())
data = input().split()

directions = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for d in data:
    for i in range(4):
        if d == directions[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            x = nx
            y = ny

print(x, y)
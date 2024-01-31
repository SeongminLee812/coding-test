n = int(input())
x, y = 0, 0

dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

# 답 저장
ans = -1

t = 0

def move(move_dir, dist):
    global x, y
    global ans, t

    for _ in range(dist):
        x += dxs[move_dir]
        y += dys[move_dir]

        t += 1

        if x == 0 and y == 0:
            ans = t
            return True
    return False

move_dirs = {'E': 0, 'W': 1, 'S': 2, 'N': 3}

for _ in range(n):
    c_dir, dist = input().split()
    dist = int(dist)
    move_dir = move_dirs[c_dir]

    done = move(move_dir, dist)

    if done:
        break
print(ans)
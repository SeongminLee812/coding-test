

def go(sums: int, goal: int):
    global ans
    if sums == goal:
        ans += 1
        return
    if sums > goal:
        return
    go(sums + 1, goal)
    go(sums + 2, goal)
    go(sums + 3, goal)

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0

    go(0, n)
    print(ans)
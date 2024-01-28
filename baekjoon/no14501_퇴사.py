n = int(input())

t = [0] # 0번째 인덱스 비워두기
p = [0] # 0번째 인덱스 비워두기

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

ans = 0
def go(day: int, total: int):
    global ans
    if day == n + 1:
        ans = max(ans, total)
        return
    if day > n + 1:
        return
    # selected
    go(day + t[day], total + p[day])
    # not selected
    go(day + 1, total)

go(1, 0)
print(ans)
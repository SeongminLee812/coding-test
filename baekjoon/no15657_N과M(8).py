import sys

n, m = map(int, input().split())
ours = list(map(int, input().split()))
ours.sort()

a = [0] * m
# 같은 수 여러번 -> 중복 가능
# 비내림차순 -> start를 포함

def go(index, start, n, m):
    if index == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    for i in range(start, len(ours)):
        a[index] = ours[i]
        go(index + 1, i, n, m)

go(0, 0, n, m)

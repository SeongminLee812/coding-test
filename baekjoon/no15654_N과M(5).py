import sys

n, m  = map(int, input().split())

a = [0] * m
c = [False] * (n + 1)
ours = list(map(int, input().split()))
ours.sort()

def go(index, m):
    if index == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    for i in range(len(ours)):
        if c[i]:
            continue
        c[i] = True
        a[index] = ours[i]
        go(index + 1, m)
        c[i] = False

go(0, m)
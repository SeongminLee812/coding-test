import sys

n, m = map(int, input().split())

c = [False] * (n + 1)
a = [0] * m

ans_list = []
def go(index: int, n: int, m: int):
    if index == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    for i in range(1, n + 1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index + 1, n, m)
        c[i] = False

go(0, n, m)
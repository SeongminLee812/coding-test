import sys

n, m = map(int, input().split())
ours = list(map(int, input().split()))
ours.sort()

a = [0] * m

def go(index, n, m):
    if index == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    for i in range(len(ours)):
        a[index] = ours[i]
        go(index + 1, n, m)

go(0, n, m)
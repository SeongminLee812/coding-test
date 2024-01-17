t = int(input())


def solution(n):
    d = [0] * 12
    d[1] = 1
    d[2] = 2
    d[3] = 4
    if n < 4:
        print(d[n])
        return
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]

    print(d[n])

for _ in range(t):
    n = int(input())
    solution(n)
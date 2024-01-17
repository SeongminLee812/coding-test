n = int(input())



def tile(n: int) -> int:
    if n == 1:
        print(1)
        return
    if n == 2:
        print(2)
        return

    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2

    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    print(d[n] % 10007)

tile(n)
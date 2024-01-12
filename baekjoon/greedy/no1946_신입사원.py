import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    rangkings = []
    for _ in range(n):
        a, b = map(int, input().split())
        rangkings.append((a, b))
    rangkings.sort()

    count = 0
    min_value = 100001
    for rank in rangkings:
        if rank[1] < min_value:
            count += 1
            min_value = rank[1]
    print(count)
import sys
input = sys.stdin.readline

n = int(input())
scores = []

for _ in range(n):
    name, kr, en, math = input().split()
    scores.append((name, int(kr), int(en), int(math)))

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in scores:
    print(i[0])
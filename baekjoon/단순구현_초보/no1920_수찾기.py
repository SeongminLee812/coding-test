import sys
input = sys.stdin.readline

n = int(input())
array_a = set(map(int, input().split()))
m = int(input())
array_b = list(map(int, input().split()))

for i in array_b:
    if i in array_a:
        print(1)
    else:
        print(0)
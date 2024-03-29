import sys
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]: # 순열이 시작되는 위치 찾기
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def calc(a):
    s = 0
    for i in range(1, len(a)):
        s += abs(a[i] - a[i - 1])
    return s

n = int(input())
a = list(map(int, input().split()))

ans = -sys.maxsize
a.sort()

while True:
    s = calc(a)
    ans = max(ans, s)
    if not next_permutation(a):
        break

print(ans)

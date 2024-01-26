import sys
input = sys.stdin.readline

n = int(input())
a = [[int(i) for i in input().split()] for _ in range(n)]

one = 0
zero = 0
minus_one = 0

mapping = {1: one, 0: zero, -1: minus_one}
def check(a):
    if len(a) == 1:
        return True
    else:
        first = a[0][0]
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] != first:
                    return False
    return True

def go(a):
    if check(a):
        mapping[a[0][0]] += 1
        print(a)
    length = len(a) // 3
    # 여기 각 1/3씩 가져오는 부분을 전부 다시 구현해야함
    go(a[:length // 3][:length // 3])  # 좌측 상단
    go(a[:length // 3][length // 3:length // 3 * 2])
    go(a[:length // 3][length // 3 * 2:])
    go(a[length // 3:length // 3 * 2][:length // 3]) # 중간
    go(a[length // 3:length // 3 * 2][length // 3:length // 3 * 2])
    go(a[length // 3:length // 3 * 2][length // 3 * 2:])
    go(a[length // 3 * 2:][:length // 3])
    go(a[length // 3 * 2:][length // 3:length // 3 * 2])
    go(a[length // 3 * 2:][length // 3 * 2:])

go(a)
print(minus_one)
print(zero)
print(one)

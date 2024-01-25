import sys

l, c = map(int, input().split())

alpha = input().split()
alpha.sort()
ans = [0] * l

moum = [ord('a'), ord('e'), ord('o'), ord('i'), ord('u')]
jaum = [chr(i) for i in range(ord('a'), ord('z') + 1)
        if i not in moum]
moum = [chr(i) for i in moum]

# 최소 1개의 모음, 최소 2개의 자음으로 구성되어있는 지 검사
def check(ans):
    jaum_cnt = 0
    moum_cnt = 0
    for a in ans:
        if a in moum:
            moum_cnt += 1
        else:
            jaum_cnt += 1
    if moum_cnt >= 1 and jaum_cnt >= 2:
        return True
    return False

# 브루트 포스 함수 구현
def go(index, start, l, c):
    if index == l:
        if check(ans):
            sys.stdout.write(" ".join(map(str, ans)) + "\n")
        return
    for i in range(start, c):
        ans[index] = alpha[i]
        go(index + 1, i + 1, l, c)

go(0, 0, l, c)
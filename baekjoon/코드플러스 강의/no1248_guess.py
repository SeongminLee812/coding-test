def check(index):
    s = 0
    for i in range(index, - 1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True

def go(index):
    if index == n:
        return True
    if sign[index][index] == 0: # 자기 자신(A[index])의 부호체크
        ans[index] = 0 # 답은 0임
        return check(index) and go(index + 1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and go(index + 1):
            return True
    return False

n = int(input())
s = input()
sign = [[0] * n for _ in range(n)]
ans = [0] * n
cnt = 0
for i in range(n): # input 받은 s 를 2차원 리스트로 변환
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

go(0)
print(" ".join(map(str, ans)))
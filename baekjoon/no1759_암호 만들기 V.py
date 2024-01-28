def check(password):
    jaum: int = 0
    moum: int = 0
    for s in password:
        if s in 'aeiou':
            moum += 1
        else:
            jaum += 1
    if jaum >= 2 and moum >= 1:
        return True
    else:
        return False

def go(alpha, password, length, i):
    if len(password) == length:
        if check(password):
            print(password)
        return
    if i >= len(alpha):
        return

    # 선택하는 경우
    go(alpha, password + alpha[i], l, i + 1)
    # 선택하지 않은 경우
    go(alpha, password, l, i + 1)

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
go(alpha, "", l, 0)


n = int(input())
c = [False] * 10
oper_list = input().split()

def check(x, y, oper):
    if oper == '<':
        return x < y
    if oper == '>':
        return x > y

def go(index, num):
    if index == n + 1:
        ans.append(num)
        return
    for i in range(0, 10):
        if c[i]:
            continue
        if index == 0 or check(num[index - 1], str(i), oper_list[index - 1]):
            c[i] = True
            go(index + 1, num + str(i))
            c[i] = False

ans = []
go(0, '')
print(max(ans))
print(min(ans))
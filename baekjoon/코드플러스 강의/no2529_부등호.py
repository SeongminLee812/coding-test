def good(x: int, y: int, oper: str) -> bool:
    if oper == '<':
        return x < y
    else:
        return x > y

def go(index, num):
    if index == n + 1:
        ans.append(num)
        return

    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(num[index - 1], str(i), a[index - 1]):
            check[i] = True
            go(index + 1, num + str(i))
            check[i] = False

check = [False] * 10

n = int(input())
a = input().split()
ans = []
go(0, '')
print(max(ans))
print(min(ans))
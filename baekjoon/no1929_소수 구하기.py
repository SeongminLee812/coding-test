# 에라토스테네스의 체

MAX = 1000000

check = [False] * (MAX + 1)
check[0] = check[1] = True

for i in range(2, MAX + 1):
    if not check[i]:
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i

m, n = map(int, input().split())

ans = []
for i in range(m, n + 1):
    if not check[i]:
        ans.append(str(i))

print('\n'.join(map(str, ans)) + '\n')


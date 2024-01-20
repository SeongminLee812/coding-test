def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

# N 이하의 소수 전체 찾기
# 에라토스테네스의 체
# 2개의 배열 필요
MAX = 1000000
check = [False] * (MAX + 1)
check[0] = True
check[1] = True

for i in range(2, MAX + 1):
    if not check[i]:
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i # i의 배수로 만듬

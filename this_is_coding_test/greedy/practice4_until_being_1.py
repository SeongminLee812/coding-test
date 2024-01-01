
# 내 답안
# n, k = map(int, input().split())
#
# count = 0
# while True:
#     if n % k == 0:
#         n /= k
#     else:
#         n -= 1
#
#     count += 1
#
#     if n == 1:
#         break
#
# print(count)


# 교재 답안

n, k = map(int, input().split())

result = 0
while True:
    # n을 k로 나누어 떨어지는 수로 만들고, 그 차이만큼 1 빼는 연산 수행
    target = (n // k) * k
    result += n - target
    n = target
    # n 이 k보다 작으면 나누어 떨어지지 않으니까 탈출
    if n < k:
        break
    n /= k
    result += 1

result += (n - 1)
print(result)


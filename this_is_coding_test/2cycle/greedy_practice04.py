# n, k = map(int, input().split())
#
# count = 0
#
# while n != 1:
#     if n % k == 0:
#         n /= k
#         count += 1
#     else:
#         n -= 1
#         count += 1
#
# print(count)

# n이 100억 이상 큰 수를 가졌을 때
n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k # n이 k의 배수가 되도록 하는 수 target을 만들기
    result += (n - target) # target과 n의 차이만큼 1을 빼는 연산을 수행했다고 가정
    n = target
    if n < k: # n이 k보다 작으면 더이상 나눌 수 없음 -> 반복문 탈출
        break
    result += 1
    n //= k

result += (n - 1)
print(result)


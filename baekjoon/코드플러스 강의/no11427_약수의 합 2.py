# 모든 약수를 더한 값
# 약수는 배수의 반대인 성질을 이용한다.
# N 이하의 자연수 중 1을 약수로 갖는 개수는 n // 1개다
# n 이하의 자연수 중 1의 배수를 찾으면 되는 문제로 변환
# n 이하의 자연수를 전부 돌면서

n = int(input())

result = 0
for i in range(1, n + 1):
    result += (n // i) * i

print(result)
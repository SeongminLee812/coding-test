# 약수들은 서로 대칭임을 이용, 최대값과 최솟값을 곱하기

n = int(input())

yaksus = list(map(int, input().split()))

print(max(yaksus) * min(yaksus))


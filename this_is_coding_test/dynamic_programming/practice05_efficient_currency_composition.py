n, m = map(int, input().split())

d = [10001] * m
d[0] = 0

currency_list = []
for i in range(n):
    temp_input = int(input())
    currency_list.append(temp_input)
    d[temp_input] = 1

min_currency = min(currency_list)

for i in range(min_currency, m):
    temp_list = []
    for j in currency_list:
        temp_list.append(d[i - j])
        print(temp_list)
        d[i] = min(temp_list) + 1

if d[m] > 10000:
    print(-1)
else:
    d[m]

# 교재 답안
n, m = map(int, input().split())

# n개의 화폐단위 입력
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 게산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# Bottom up DP
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])


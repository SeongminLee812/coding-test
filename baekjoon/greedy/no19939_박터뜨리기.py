n, k = map(int, input().split())

total_sum = int((k * (k + 1)) / 2) # 등차수열 합 공식 1 ~ k 까지 하나씩 늘어갈 때 총 합

if total_sum > n: # 등차 수열 합 보다 n이 작으면 분배 불가
    print(-1)
elif (n - total_sum) % k == 0: # 딱 맞아 떨어질 때는 가장 큰 k 와 가장 작은 1의 차이
    print(k - 1)
else: # 딱 맞아 떨어지지 않고 n이 남을 때는 가장 큰 바구니 부터 + 1 하면되므로 k + 1과 1의 차이 반환
    print(k + 1 - 1)

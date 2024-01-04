# 피보나치 수열(재귀)

# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    # print(f'f({x})', end='\t')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


# 피보나치 수열 (반복)

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫번째 피보나치 수와 두번째 수는 1
d[1] = d[2] = 1
n = 99

# 피보나치 함수를 반복문으로 구현 (bottom-up DP)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[99])

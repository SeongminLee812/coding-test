# % 연산을 먼저 하고 곱하나, 곱하고 나서 % 연산을 하나 동일하다는 점을 이용

# 각 자리가 모두 1로만 이루어진 n의 배수
#  1 % N, 11 % N, 111 % N을 계속하면서, N으로 나누어 떨어지면 그 배수다.
# 나머지만 남겨서 나머지끼리만 비교한다.
# (a x b) % c = ((a % c) * (b % c)) % c

while True:
    try:
        N = int(input())

        num = 0
        i = 1
        while True:
            num = (num * 10 + 1) % N
            if num % N == 0:
                break
            i += 1
        print(i)



    except:
        break
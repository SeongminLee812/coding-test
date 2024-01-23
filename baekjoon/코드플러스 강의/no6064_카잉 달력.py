# x가 m보다 커지면 x는 1이 됨.
# y가 n보다 커지면 y는 1이 된다.
# 전체 brute force로 구하면 시간 복잡도는 N^2 40000*40000 = 1600000000이다.
# 시간 초과

# 건너뛰면서 확인하기
# 10 12 3 9가 주어졌으면 x는 10으로 나눴을 때 3이 남는 수들이다.
# x와 y에 -1씩 해서 범위를 0 <= x <= M -1, 0 <= y <= N -1로 맞춰준다.
## 브루트 포스로 구현할 방법
### 현재 알 수 없는 부분 : 어떤 년도가 x:y에 해당하는 지 알 수 없음
# year 변수 선언
# year를 1씩 늘려가면서 -> (year - 1) % m == x일때, (year - 1) % n == y인 수 찾기,

# 종료 조건
# 만약 year가 m * n과 같아졌는데 안나오면 -> print(-1)로 끝냄
import sys
input = sys.stdin.readline

t = int(input())

answers = []

for _ in range(t):
    m, n, x, y = map(int, input().split())

    ans = 0
    last_year = n * m
    year = 0
    while year < last_year: # (year % m = x) => (year - 1) % m = x - 1 (양변에 1씩 빼주기)
        if year % m == x - 1:
            if year % n == y - 1:
                ans = year + 1
                break
            year += m
            continue
        year += 1

    if ans:
        answers.append(ans)
    else:
        answers.append(-1)

sys.stdout.write('\n'.join(map(str, answers)) + '\n')
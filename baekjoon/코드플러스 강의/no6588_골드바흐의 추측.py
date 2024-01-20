# 풀이
# 에라토스테네스의 체로 소수를 전부 구함
## 에라토스테네스의 체 : 루트n까지 돌면서 i의 배수들을 다 지운다. 가장 작은수는 소수

## 이때는 prime list에 소수를 전부 저장해둔다
## 주어진 짝수에 대하여, 검사를 실행한다
## prime list에서 하나씩 돌아가면서 target을 뺀 수가 있다면,
## for i in primes:
##     if target - i in primes:
##         print(f'{target} = {i} + {target - i}
##         break
# test case 스타일의 문제 -> 변하지 않는 값은 먼저 구해놓고 입출력만 받음
#

import sys
input = sys.stdin.readline

MAX = 1000000

check = [False] * (MAX + 1)
check[0] = check[1] = True
primes = []

for i in range(2, MAX + 1): # n lg n
    if not check[i]:
        primes.append(i)
        j = i + i # j는 i의 2배수로 시작
        while j <= MAX:
            check[j] =True
            j += i # j의 배수 순회

primes = primes[1:]
ans = []
while True:
    n = int(input())
    if n == 0:
        break
    for p in primes: # O(N)
        if not check[n - p]:
            ans.append(f'{n} = {p} + {n - p}')
            break

print('\n'.join(ans) + '\n')

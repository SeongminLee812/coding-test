
# 순서가 있는 선택하는 문제 -> 재귀
# 변하는 부분 : 위치, 앞에서 사용한 수 (뒤에서 사용할 수는 앞에서 사용한 수보다 크거나 같은 거만)
# 재귀 함수로 구현할 부분 : 어떤 수가 올 지 결정하는 부분
# 재귀 함수에 인자로 전달할 부분 : 위치, 사용할 수 있는 수(앞에서 결정된 수 + 1을 받아서 그 이후만 반복문 구현)
# 종료 조건 : m자리 숫자까지 다 결정하고 다음으로 넘어가는 순간 (index == m)
import sys

n, m = map(int, input().split())
a = [0] * m

def go(index: int, start: int, n: int, m: int):
    if index == m: # 다 결정되면
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    # 다음수로 올 수를 탐색하기
    for i in range(start, n + 1):
        a[index] = i
        go(index + 1, i + 1, n, m) # 재귀함수는 스택으로 구현된다. (DFS라고 생각해도 되는 문제?)

go(0, 1, n, m)
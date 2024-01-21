
# 1~N까지 계속 탐색할 것임
# 위치를 다음 위치로 바꿔가면서 재귀
# 또한, 선택한 수를 사용한 수로 체크(문제의 조건 -> 중복 없이)하여 사용 가능한 수의 배열을 바꿔가면서
# 재귀로 구현
# 종료 조건 고른 수가 m개 일때, 즉 index가 내가 선택하려는 수의 범위를 넘어설 때(index == m)
import sys

n, m = map(int, input().split())

c = [False] * (n + 1)
a = [0] * m

def go(index, n, m):
    """각 자리에 들어올 수를 결정하는 함수"""
    # index번째 자리 수를 결정할 것임
    if index == m: # index가 m이 되면 0, 1, 2, ..., m - 1까지 전부 채워진 것이므로 종료
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(1, n + 1): # 들어오게 될 수를 결정
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index + 1, n, m)
        c[i] = False # go 함수가 스택에 저장 -> 전부 종료된 이후에 c[i] = False로 원상 복귀시켜서 다음 수를 탐색할 수 있게함

go(0, n, m)

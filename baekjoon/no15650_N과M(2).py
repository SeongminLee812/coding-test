import sys

n, m = map(int, input().split())

a = [0] * m

def go(index, start, n, m):
    if index == m:
        sys.stdout.write(" ".join(map(str, a)) + "\n")
        return
    for i in range(start, n + 1):
        a[index] = i
        go(index + 1, i + 1, n, m)
        # 만약 a가 1, 2, 3이고 다음 1, 2, 4를 탐색할 때 3에 대한 함수는 종료되었으나
        # 2에 대한 함수는 아직 종료되지 않았으므로 for문이 돌면서 i가 4가 되어
        # 1, 2, 4를 반환함 -> 1, 2, 5도 반복
        # 즉 가장 뒤에 인덱스만 종료되고 다시 시작하다가, i가 꽉 차면
        # 그 앞 함수가 종료되고 다시 시작하기 시작함
        # 재귀 == 스택임을 기억

go(0, 1, n, m)


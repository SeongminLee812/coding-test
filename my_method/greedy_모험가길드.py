"""
1. 문제
공포도가 높을수록 공포를 많이 느끼는 사람이다.
X 공포도를 가진 사람은 X 명 이상의 그룹에 속해야 그룹을 형성할 수 있다.
모험을 떠날 수 있는 최대 그룹수를 구하라 ( 단, 모든 사람이 그룹이 결성이 되지 않아도 된다. )
입력 조건
N 명 , 전체 인원 수
모험가의 공포도 간격을 두고 N 개수 만큼 들어온다.
출력 조건
모험을 떠날 수 있는 최대 그룹수를 구하라.

입력 예시
5
2 2 1 2 3
출력 예시
2
"""
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
count = 0

for d in data:
    count += 1
    if d <= count:
        result += 1
        count = 0

print(result)


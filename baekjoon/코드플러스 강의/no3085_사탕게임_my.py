# 풀이
## 체크하는 함수를 만듬
## 체크하는 함수는 나와 붙어있는 4방향을 검사하는데, 결국 [0][0]에서 시작해서
## 오른쪽에 연속되는 것 확인해서 +1, 아래쪽에 연속되는거 확인해서 +1
## 연속되면 더 진행하면서 + 1

## 교환하는 과정
## 상하좌우 4칸 다 볼 필요 없이 오른쪽과 아랫쪽만 교환하면됨
## 교환 후 체크, 다시 원상복구
from typing import *

n = int(input())
a = [list(input()) for _ in range(n)]
def check(a: List[List[str]]) -> int:
    ans = 0
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if a[i][j] == a[i][j + 1]:
                cnt += 1
                if ans < cnt:
                    ans = cnt
            else:
                cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if a[j][i] == a[j + 1][i]: # 아랫줄과 연속이면
                cnt += 1
                if ans < cnt: # 가장 큰 cnt 찾기
                    ans = cnt
            else:
                cnt = 1
        if ans < cnt:
            ans = cnt
    return ans

# 우로 한칸 바꾼 후 비교하기
ans = 0
for i in range(n):
    for j in range(n - 1):
        a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j] # 우로 바꾸기
        cnt = check(a) # 가장 긴 열or행 체크
        if ans < cnt:
            ans = cnt
        a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j] # 원상복구

for i in range(n):
    for j in range(n - 1):
        a[j][i], a[j + 1][i] = a[j + 1][i], a[j][i] # 아래로 바꾸기
        cnt = check(a) # 가장 긴 열or행 체크
        if ans < cnt:
            ans = cnt
        a[j][i], a[j + 1][i] = a[j + 1][i], a[j][i] # 원상복구

print(ans)
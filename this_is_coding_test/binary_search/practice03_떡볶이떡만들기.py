import sys

n, m = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(data)

result = 0
while start < end:
    mid = (start + end) // 2
    sums = sum([x - mid for x in data if x > mid])
    if sums == m:
        break
    elif sums < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(mid)


# 교재 답안

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(data)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in data:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 왼쪽 부분 탐색
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 오른쪽 부분 탐색
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답출력
print(result)


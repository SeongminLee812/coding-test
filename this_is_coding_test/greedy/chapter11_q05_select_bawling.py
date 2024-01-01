# 내 답안
# import sys
#
# n, m = map(int, input().split())
#
# ball_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# count = 0
# for i in range(n - 2):
#     compare_list = [remain for remain in ball_list[i + 1:] if remain != ball_list[i]]
#     print(compare_list)
#     count += len(compare_list)
#
# if ball_list[-1] != ball_list[-2]:
#     count += 1
#
# print(count)

# 교재 답안
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11
for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

print(array)
result = 0

# 1부터 m까지의 각 무게에 대해 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)
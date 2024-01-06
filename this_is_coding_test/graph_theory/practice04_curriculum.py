from collections import deque
import sys
import copy

# 내 답안
# input = sys.stdin.readline
#
# lecture_num = int(input())
#
# graph = [[] for _ in range(lecture_num + 1)]
# indegree = [0] * (lecture_num + 1)
# lecture_time = [0] * (lecture_num + 1)
#
# for i in range(1, lecture_num + 1):
#     data = [int(s) for s in input().split()]
#     for idx, j in enumerate(data):
#         if j == -1:
#             break
#         if idx != 0:
#             graph[j].append(i)
#             indegree[i] += 1
#     lecture_time[i] = data[0]
#
# q = deque()
# result = copy.deepcopy(lecture_time)
#
# for i in range(1, lecture_num + 1):
#     if indegree[i] == 0:
#         q.append(i)
#
# while q:
#     now = q.popleft()
#     print(result[now])
#
#     for i in graph[now]:
#         indegree[i] -= 1
#         result[i] = max(result[i], result[now] + lecture_time[i])
#         if indegree[i] == 0:
#             q.append(i)



# test case
"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""


# 교재 답안

# 노드 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드들에 대한 간선 정보를 받기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보 입력 받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 담음
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])

topology_sort()

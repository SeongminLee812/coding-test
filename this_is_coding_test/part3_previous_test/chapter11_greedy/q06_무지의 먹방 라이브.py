import heapq

food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(1, len(food_times)):
        heapq.heappush(q, (food_times[i], i))

    sum_value = 0
    previous = 0
    left_food = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * left_food) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * left_food
        left_food -= 1 # 다 먹은 음식 제외
        previous = now # 이전음식 재설정

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % left_food][1]

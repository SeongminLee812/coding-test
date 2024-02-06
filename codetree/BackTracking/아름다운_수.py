n = int(input())
total = 0
ans = []


def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치
    i = 0
    while i < n:
        # 정답 칸을 넘어버리는 경우
        # 즉 해당 숫자가 더이상 연속하여 나올 수 없는 경우 False
        if i + ans[i] - 1 >= n:
            return False
        # 하나라도 다른 숫자가 있는 지 확인
        for j in range(i, i + ans[i]):
            if ans[j] != ans[i]:
                return False

        i += ans[i]

    return True


def choose(index):
    global ans, total
    if index == n:
        if is_beautiful():
            total += 1
        return
    for i in range(1, 5):
        ans.append(i)
        choose(index + 1)
        ans.pop()

choose(0)
print(total)
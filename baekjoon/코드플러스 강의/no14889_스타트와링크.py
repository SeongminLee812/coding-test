def go(index, first, second):
    # 종료조건
    if index == n:
        if len(first) != n // 2:
            return -1
        if len(second) != n // 2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n // 2):
            for j in range(n // 2):
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff

    # 검사 선행
    if len(first) > n // 2:
        return -1
    if len(second) > n // 2:
        return -1

    ans = -1
    t1 = go(index + 1, first + [index], second) # 첫번쨰 팀 할당했을 때 경우의수
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index + 1, first, second + [index]) # 두번째 팀에 할당
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))


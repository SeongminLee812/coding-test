def next_permutation(a):
    # 내림차순 찾기
    i = len(a) - 1
    while i > 0 and a[i - 1] > a[i]: # while문에서 빠져 나오는 경우 내림차순이 끝난 것
        i -= 1
    if i <= 0: # 다음순열이 없는 경우
        return False

    j = len(a) - 1
    while a[i - 1] > a[j]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))

if not next_permutation(a):
    print(-1)
else:
    print(" ".join(map(str, a)))

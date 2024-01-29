def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] < a[i]: # 오름차순 찾기
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[i - 1] < a[j]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j :
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))

if not prev_permutation(a):
    print(-1)
else:
    print(" ".join(map(str, a)))
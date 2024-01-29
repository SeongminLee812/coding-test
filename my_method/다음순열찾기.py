def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]: # 내림차순(비오름차순)인 경우
        i -= 1
    if i <= 0:
        return False # 다음 순열이 없는 경우 (이 순열이 마지막 순열)
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    # j 위치부터 뒤 배열 전부 뒤집기
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # 슬라이싱으로 뒤집기 사용
    # a[i:] = a[i:][::-1]

    return True

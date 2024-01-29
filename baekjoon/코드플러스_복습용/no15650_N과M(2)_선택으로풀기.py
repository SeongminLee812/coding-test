def go(index, selected, n, m):
    """
    재귀적으로 수를 선택하는 함수
    :param index: 1 ~ n까지의 숫자를 의미함
    :param selected: 몇번째 선택인지 의미
    :param n: 문제의 조건 1 (1 <= M <= N <= 8)
    :param m: 문제의 조건 2
    :return: 없음
    """
    if selected == m:
        print(' '.join(map(str, a)))
        return
    if index > n:
        return

    a[selected] = index
    go(index + 1, selected + 1, n, m)
    a[selected] = 0
    go(index + 1, selected, n, m)

n, m = map(int, input().split())
a = [0] * m

go(1, 0, n, m)
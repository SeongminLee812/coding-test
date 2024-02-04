def print_star(n):
    if n == 0:
        return
    print_star(n - 1)
    print('*' * 5, n)

print_star(5)
# 제일 마지막에 호출된게 먼저 나오고, 가장 먼저 호출된게 마지막에 나옴
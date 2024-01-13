n = int(input())

left_space = n - 1
star = 1

for _ in range(n):
    print(' ' * left_space + '*' * star)
    left_space -= 1
    star += 2

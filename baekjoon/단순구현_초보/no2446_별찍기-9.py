n = int(input())

for i in range(n - 1, -1, -1):
    space = n - i - 1
    stars = i * 2 + 1
    print(' ' * space + '*' * stars)

space = 0
stars = 0
for i in range(1, n):
    space = n - i - 1
    stars = i * 2 + 1
    print(' ' * space + '*' * stars)

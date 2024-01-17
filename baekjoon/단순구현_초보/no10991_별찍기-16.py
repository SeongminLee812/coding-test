n = int(input())

left = n - 1

for i in range(n):
    print(' ' * left + '*' + ' *' * i)
    left -= 1
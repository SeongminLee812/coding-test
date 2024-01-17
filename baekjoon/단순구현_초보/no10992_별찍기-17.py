n = int(input())

left = n - 1
middle = -1

while left:
    if middle > 0:
        print(' ' * left + '*' + ' ' * middle + '*')
    else:
        print(' ' * left + '*')
    left -= 1
    middle += 2


last = (2 * n) - 1
print('*' * last)
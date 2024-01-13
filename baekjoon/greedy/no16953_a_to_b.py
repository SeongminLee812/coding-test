A, B = map(int, input().split())

count = 1

n, m = A, B

while True:
    if n == m:
        print(count)
        break
    elif n > m:
        print(-1)
        break
    else:
        str(m)[-1]
        if str(m)[-1] == '1':
            m = int(str(m)[:-1])
            count += 1
        elif m % 2 == 0:
            m //= 2
            count += 1
        else:
            print(-1)
            break


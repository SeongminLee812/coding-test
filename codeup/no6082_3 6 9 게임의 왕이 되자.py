n = int(input())
target = [3, 6, 9]


for i in range(1, n + 1):
    for n in target:
        if str(n) in str(i):
            i = 'X'
    print(i, end=' ')
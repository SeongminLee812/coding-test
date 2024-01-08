d = [0] * 100

def fibo(x):
    print(f'f({x})', end=' ')
    if x == 0 or x == 1:
        d[x] = 1
    if d[x] == 0:
        d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(6))

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

# bottom up
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
num = int(input())

n = 0
c = 0
while True:
    c += 1
    n += c
    if n >= num:
        break
print(n)
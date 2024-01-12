a, b, c, m = map(int, input().split())

x, y = 0, 0 # 일한 시간, 쉰 시간
p = 0 # 피로도
s_time = 0 # 소요 시간

result = 0 # 출력값, b * x가 될 것임

while True:
    if a > m:
        break
    if p <= 0:
        p = 0
    if p + a <= m:
        x += 1
        p += a
    else:
        y += 1
        p -= c
    s_time += 1
    if s_time == 24:
        break

result = x * b
print(result)
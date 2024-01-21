# e, s, m은 1씩 시작
# 다 1씩 더해줌
# 자기 범위를 넘어가면 다시 1로 바꿔준다.

e, s, m = map(int, input().split())

n = 1
e1 = s1 = m1 = 1
while True:
    if e1 > 15:
        e1 = 1
    if s1 > 28:
        s1 = 1
    if m1 > 19:
        m1 = 1
    if e1 == e and s1 == s and m1 == m:
        break
    e1 += 1
    s1 += 1
    m1 += 1
    n += 1

print(n)
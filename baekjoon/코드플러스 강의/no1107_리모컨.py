# 이동하려는 채널 n
# n과의 차이
# 무조건 처음은 숫자를 통해 이동 -> 이후 +/- 버튼으로 이동
# 아예 숫자를 누르지 않는 경우가 빠를 수 있으므로 초기값을 +/-만 누른 것으로 설정
# +/- 버튼 수는 abs(n - c)
# 1. 이동하려는 채널
# 2. 해당 채널까지 가는 경로 전부 탐색 (0~100만)
#   - 그 숫자를 내가 누를 수 있는 숫자인지 검사
#   - 문자열 파싱하기(x) -> c % 10이 broken에 True인지 검사
#   - 검사 후 이상 없으면 c //= 10으로 1의 자리 수 제외 후 다시검사
# 3. 내가 이동한 숫자버튼 - n의 절대값만큼 +/- 입력
# 두 수 합해준 후 초기값과 비교 하여 최소값 탐색

n = int(input())
m = int(input())

broken = [False] * 10
if m > 0:
    a = list(map(int, input().split()))
    for x in a:
        broken[x] = True

def possible(c: int) -> int:
    """해당 채널로 이동이 가능한 지 검사, 가능하면 버튼의 자리수 반환"""
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if not broken[c % 10]: # 1의 자리 수부터 검사
            l += 1
            c //= 10
        else:
            return 0
    return l

ans = abs(n - 100)
for i in range(0, 1000000 + 1):
    c = i
    l = possible(c)
    press = 0
    if l:
        press += l + abs(n - c)
        if ans > press:
            ans = press

print(ans)
# 입력 받기
n = int(input())
arr = [0] + list(map(int, input().split()))

# 일단 최소공배수 구하기
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

def get_lcm_all(index):
    # index가 단 하나만 남았을 때는 자기 자신 반환
    if index == 1:
        return arr[index]

    return lcm(get_lcm_all(index - 1), arr[index])

print(get_lcm_all(n))
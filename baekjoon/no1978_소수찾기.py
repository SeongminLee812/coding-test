import math
def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1): # 약수는 해당 수의 제곱근까지만 확인하면 됨
        if num % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))

count = 0

for n in nums:
    if is_prime(n):
        count += 1

print(count)
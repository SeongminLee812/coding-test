from typing import *
def max_sum(N: int, M: int, K: int, nums:List[int]) -> int:
    nums.sort()
    first = nums[-1]
    second = nums[-2]
    result = 0

    while M:
        for _ in range(K):
            result += first
            M -= 1
        result += second
        M -= 1

    return result




def max_sum(N: int, M: int, K: int, nums:List[int]) -> int:
    nums.sort()
    first = nums[-1]
    second = nums[-2]

    loop_num = first * K + second
    mok, remain = divmod(M, K+1)
    sums = mok * loop_num + remain * first
    return sums

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

print(max_sum(N, M, K, nums))

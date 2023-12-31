from bisect import bisect_left, bisect_right
from typing import *

a = [1, 2, 4, 4, 8]

print(bisect_left(a, 4))
print(bisect_right(a, 4))

def count_by_range(a: List[int], x: int, y: int) -> int:
    left = bisect_left(a, x)
    right = bisect_right(a, y)

    return right - left

a = [1, 2,3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, 2, 4))
from typing import *
def sum_even(num: int) -> int:
    sums = 0
    for i in range(0, num + 1, 2):
        sums += i

    return sums

print(sum_even(8))
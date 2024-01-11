from itertools import permutations
# 브루트 포스 -> 메모리 초과

"""
n = input()

if '0' not in n:
    print(-1)
else:
    n_list = list(permutations(n, len(n)))
    for i in n_list:
        i = int(''.join(i))
        if i % 30 == 0:
            print(i)
            break
"""

n = input()

if '0' not in n:
    print(-1)
else:
    total = 0
    for s in n:
        total += int(s)
    if total % 3 == 0:
        result = int(''.join(sorted(n, reverse=True)))
        print(result)
    else:
        print(-1)
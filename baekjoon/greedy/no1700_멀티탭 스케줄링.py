n, k = map(int, input().split())

use_list = list(map(int, input().split()))
concent = []
result = 0

for now in range(k):
    if use_list[now] in concent:
        pass

    if len(concent) < n:
        concent.append(use_list[now])
        continue

    priority = []
    for c in concent:
        if c in use_list[now:]: # 다음에 또 이용해야하는 경우
            priority.append(use_list[now:].index(c))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    concent.remove(concent[target])
    concent.append(use_list[now])
    result += 1

print(result)


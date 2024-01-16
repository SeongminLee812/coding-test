t_list = []

first = 0
for i in range(1, 300):
    first += i
    if first >= 1000:
        break
    t_list.append(first)

test_case = int(input())
k_list = []

for _ in range(test_case):
    k_list.append(int(input()))

for k in k_list:
    result = 0
    for t1 in t_list:
        for t2 in t_list:
            now = k - t1 - t2
            if now in t_list:
                result = 1
                break
        if result == 1:
            break
    print(result)

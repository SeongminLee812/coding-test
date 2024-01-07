# n = int(input())
# results = []
#
# for _ in range(n):
#     name, score = input().split()
#     results.append((name, int(score)))
#
# results = sorted(results, key = lambda x: x[1])
#
# for name, score in results:
#     print(name, end=' ')

# 계수정렬 구현
n = int(input())

results = []

max_value = 0
for _ in range(n):
    input_data = input().split()
    input_data[1] = int(input_data[1])
    results.append((input_data[0], input_data[1]))
    max_value = max(max_value, input_data[1])

count_table = [0] * (max_value + 1)
name_list = [[] for _ in range(max_value + 1)]

for name, score in results:
    print(name, score)
    count_table[score] += 1
    name_list[score].append(name)

print(count_table)
print(name_list)
for name, score_count in zip(name_list, count_table):
    if name:
        for n in name:
            print(n)
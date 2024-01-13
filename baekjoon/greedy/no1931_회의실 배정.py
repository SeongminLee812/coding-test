n = int(input())

confer_list = []
for _ in range(n):
    a, b = map(int, input().split())
    confer_list.append((a, b))

def sort1(x):
    return x[1], x[0]

sorted_list = sorted(confer_list, key=sort1)


for i, (a, b) in enumerate(sorted_list):
    if i == 0:
        count = 1
        finished = b
        continue
    if a >= finished:
        count += 1
        finished = b
print(count)
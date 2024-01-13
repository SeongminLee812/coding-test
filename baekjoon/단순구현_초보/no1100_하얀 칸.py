
ground = [[] for _ in range(8)]

for row in range(8):
    line = input()
    for elem in line:
        ground[row].append(elem)

result = 0
for i in range(8):
    if i % 2 == 0: # 홀수 행 일때
        for j in range(0, 8, 2):
            if ground[i][j] == 'F':
                result += 1
    else:
        for j in range(1, 8, 2):
            if ground[i][j] == 'F':
                result += 1

print(result)

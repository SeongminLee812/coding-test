
steps =[(2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (-1, 2)]

coor = input()
x_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
x = x_dict[coor[0]]
y = int(coor[1])

result = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    result += 1

print(result)
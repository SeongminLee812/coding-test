n, m = map(int, input().split())

min_val = 65

chess_w = [list('WB') * 4, list('BW') * 4, list('WB') * 4, list('BW') * 4, list('WB') * 4, list('BW') * 4, list('WB') * 4, list('BW') * 4]
chess_b = [list('BW') * 4, list('WB') * 4, list('BW') * 4, list('WB') * 4, list('BW') * 4, list('WB') * 4, list('BW') * 4, list('WB') * 4]

graph = []
for _ in range(n):
    line = list(input())
    graph.append(line)

for i in range(n):
    for j in range(m):
        if i + 8 > n or j + 8 > m:
            continue

        count_1 = 0
        count_2 = 0
        for row in range(8):
            for col in range(8):
                if graph[i + row][j + col] != chess_w[row][col]:
                    count_1 += 1

        for row in range(8):
            for col in range(8):
                if graph[i + row][j + col] != chess_b[row][col]:
                    count_2 += 1


        min_val = min(min_val, count_1, count_2)

print(min_val)
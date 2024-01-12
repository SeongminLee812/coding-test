n = int(input())

distances = list(map(int, input().split()))
oil_val = list(map(int, input().split()))

min_value = 1000000001

total_cost = 0

for i in range(len(distances)):
    min_value = min(min_value, oil_val[i])
    total_cost += min_value * distances[i]

print(total_cost)

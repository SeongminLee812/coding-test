n = int(input())

age_name = []

for k in range(n):
    a, b = input().split()
    age_name.append((int(a), b, int(k)))

age_name.sort(key=lambda x: (x[0], x[2]))

for i, j, k in age_name:
    print(i, j)
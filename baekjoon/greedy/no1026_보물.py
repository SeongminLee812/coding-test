n = int(input())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

result = 0

for i in range(n):
    result += array_a[i] * array_b[i]

print(result)
n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

print(sorted(nums, reverse=True))
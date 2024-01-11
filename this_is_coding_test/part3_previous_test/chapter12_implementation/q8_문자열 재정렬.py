S = input()

strings = []
nums = []

for s in S:
    if s.isalpha():
        strings.append(s)
    else:
        nums.append(s)

strings.sort()

print(''.join(strings) + str(sum(map(int, nums))))
data = input()

zeros = 0
ones = 0

if data[0] == '0':
    zeros += 1
else:
    ones += 1

for i in range(1, len(data)):
    if data[i - 1] != data[i]:
        if data[i] == '0':
            zeros += 1
        else:
            ones += 1

print(min(zeros, ones))
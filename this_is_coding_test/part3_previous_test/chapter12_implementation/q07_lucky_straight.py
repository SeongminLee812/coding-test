#
# n = input()
#
# idx = len(n) // 2
# s1, s2 = n[:idx], n[idx:]
#
# if sum(map(int, s1)) == sum(map(int, s2)):
#     print('LUCKY')
# else:
#     print('READY')


n = input()

idx = len(n) // 2

summary = 0
for i in range(idx):
    summary += int(n[i])

for i in range(idx, len(n)):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')

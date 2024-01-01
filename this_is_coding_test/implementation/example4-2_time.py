n = int(input())

times = n * (60 * 60) - 1

count = 0
hour = 0
minute = 0
second = 0

for i in range(times, 0, -1):

    hour = str(i // 3600)
    minute = str(i % 3600 // 60)
    second = str(i % 3600 % 60)
    print(f'{hour} : {minute} : {second}')

    if '3' in hour + minute + second:
        print('check!!!')
        count += 1

print(count)


# 교재 답안
# H 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)



